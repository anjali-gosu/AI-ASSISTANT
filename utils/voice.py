import pyttsx3
import speech_recognition as sr

# 🔥 Initialize engine
engine = pyttsx3.init()

# 🔥 Get available voices
voices = engine.getProperty('voices')

# 🔥 Set voice (try 0 or 1 if needed)
engine.setProperty('voice', voices[0].id)

# 🔥 Adjust properties
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)

def speak(text):
    print("🤖 Jarvis:", text)
    
    try:
        engine.stop()  # 🔥 prevents voice freeze issues
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("Voice Error:", e)

def listen():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        return command.lower()
    except:
        return ""
