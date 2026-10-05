import random
import threading
import webbrowser
import sys
import queue

from PySide6.QtWidgets import QApplication

from utils.voice import speak, listen
from assistant.commands import handle_command
from assistant.brain import ask_ai
from gui.interface import JarvisGUI


def run_jarvis(gui):
    # Create queue for text commands from GUI
    text_queue = queue.Queue()
    
    # Set callback for GUI text input
    gui.text_command_callback = lambda cmd: text_queue.put(cmd)

    speak("Initializing Jarvis")
    gui.statusSignal.emit("Listening")

    speak("System ready")
    gui.update_status("Idle")

    responses = [
        "Yes?",
        "I'm listening",
        "Go ahead",
        "Tell me"
    ]

    wake_words = [
        "hey",
        "jarvis",
        "jar",
        "heyy jar",
        "bangaram",
        "chintu",
        "chinna"
    ]

    active = False

    while True:

        gui.update_status("Listening")
        gui.update_response("Listening...")

        # Check for text command first (non-blocking)
        is_text_command = False
        try:
            command = text_queue.get_nowait()
            print("📝 Text Input:", command)
            is_text_command = True
        except queue.Empty:
            # No text command, use voice
            command = listen()

        if command == "":
            continue

        print("👤 You:", command)

        gui.commandSignal.emit(command)

        cmd = command.lower()

        # 🔥 WAKE WORD (only for voice commands)
        if not active and not is_text_command:

            if any(word in cmd for word in wake_words):

                active = True

                gui.update_status("Activated")

                speak(random.choice(responses))

            continue

        # 🔧 PROCESS COMMAND
        gui.update_status("Processing")
        gui.responseSignal.emit(response)

        result = handle_command(cmd)

        # 🔚 EXIT
        if result == "exit":

            gui.update_status("Shutting down")

            speak("Goodbye")

            gui.update_response("Goodbye")

            break

        # 🤖 AI / SEARCH
        if not result:

            try:
                gui.update_status("Thinking")

                response = ask_ai(cmd)

            except:

                response = "Searching on Google"

                webbrowser.open(
                    f"https://www.google.com/search?q={cmd}"
                )

            gui.update_status("Speaking")

            gui.update_response(response)

            speak(response)

        gui.update_status("Idle")


if __name__ == "__main__":

    app = QApplication(sys.argv)

    gui = JarvisGUI()

    jarvis_thread = threading.Thread(
        target=run_jarvis,
        args=(gui,),
        daemon=True
    )

    jarvis_thread.start()

    gui.show()

    sys.exit(app.exec_())