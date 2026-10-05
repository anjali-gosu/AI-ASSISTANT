import webbrowser
import datetime
import os
import subprocess
import cv2
import pywhatkit
import pyautogui
import psutil
from utils.voice import speak


def handle_command(command):

    cmd = command.lower()

    # 🔹 TIME
    if "time" in cmd:
        time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {time}")
        return True

    # 🔹 GOOGLE
    elif "google" in cmd:
        speak("Opening Google")
        webbrowser.open("https://google.com")
        return True

    # 🔹 YOUTUBE
    elif "youtube" in cmd:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
        return True

    # 🔹 PLAY SONG
    elif "play" in cmd:
        song = cmd.replace("play", "")
        speak(f"Playing {song}")
        pywhatkit.playonyt(song)
        return True

    # 🔹 SEARCH GOOGLE
    elif "search" in cmd:
        search = cmd.replace("search", "")
        speak(f"Searching {search}")
        pywhatkit.search(search)
        return True

    # 🔹 NOTEPAD
    elif "notepad" in cmd:
        speak("Opening Notepad")
        os.system("notepad")
        return True

    # 🔹 CALCULATOR
    elif "calculator" in cmd:
        speak("Opening Calculator")
        os.system("calc")
        return True

    # 🔹 CAMERA
    elif "camera" in cmd:
        speak("Opening Camera")

        cam = cv2.VideoCapture(0)

        while True:
            ret, frame = cam.read()

            if not ret:
                break

            cv2.imshow("Camera", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cam.release()
        cv2.destroyAllWindows()
        return True

    # 🔹 VS CODE
    elif "vs code" in cmd or "vscode" in cmd:
        speak("Opening Visual Studio Code")
        os.system("code")
        return True

    # 🔹 SPOTIFY
    elif "spotify" in cmd:
        speak("Opening Spotify")
        os.system("start spotify")
        return True

    # 🔹 FILE EXPLORER
    elif "file explorer" in cmd:
        speak("Opening File Explorer")
        os.system("explorer")
        return True

    # 🔹 WHATSAPP WEB
    elif "whatsapp" in cmd:
        speak("Opening WhatsApp")
        webbrowser.open("https://web.whatsapp.com")
        return True

    # 🔹 SCREENSHOT
    elif "screenshot" in cmd:
        speak("Taking Screenshot")

        screenshot = pyautogui.screenshot()

        screenshot.save("screenshot.png")

        speak("Screenshot saved")
        return True

    # 🔹 BATTERY
    elif "battery" in cmd:
        battery = psutil.sensors_battery()

        percent = battery.percent

        speak(f"Battery is at {percent} percent")
        return True

    # 🔹 VOLUME UP
    elif "volume up" in cmd:
        pyautogui.press("volumeup")
        speak("Volume increased")
        return True

    # 🔹 VOLUME DOWN
    elif "volume down" in cmd:
        pyautogui.press("volumedown")
        speak("Volume decreased")
        return True

    # 🔹 MUTE
    elif "mute" in cmd:
        pyautogui.press("volumemute")
        speak("Volume muted")
        return True

    # 🔹 LOCK SYSTEM
    elif "lock system" in cmd:
        speak("Locking system")
        os.system("rundll32.exe user32.dll,LockWorkStation")
        return True

    # 🔹 SHUTDOWN PC
    elif "shutdown computer" in cmd:
        speak("Shutting down computer")
        os.system("shutdown /s /t 5")
        return True

    # 🔹 RESTART PC
    elif "restart computer" in cmd:
        speak("Restarting computer")
        os.system("shutdown /r /t 5")
        return True

    # 🔹 EXIT JARVIS
    elif "shutdown" in cmd or "exit" in cmd:
        return "exit"

    # 🔹 OPEN ANY APP
    elif "open" in cmd:

        app = cmd.replace("open", "").strip()

        speak(f"Opening {app}")

        try:
            os.system(f"start {app}")
            return True
        except:
            return False

    return False