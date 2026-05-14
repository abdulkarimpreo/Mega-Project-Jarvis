import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

recognizer = sr.Recognizer()

def speak(text):
    engine = pyttsx3.init()   # ✅ Reinitialize each time
    engine.say(text)
    engine.runAndWait()
    engine.stop()             # ✅ Fully release audio driver

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)


if __name__ == "__main__":
    speak("Initializing Jarvis....")
    
    r = sr.Recognizer()  # ✅ Create once, outside the loop
    
    while True:
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            
            word = r.recognize_google(audio)
            print(f"Heard: {word}")
            
            if word.lower() == "jarvis":
                speak("Ya")  # ✅ Now works correctly
                
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                    command = r.recognize_google(audio)
                    processCommand(command)
                    
        except Exception as e:
            print("Error: {0}".format(e))