import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import os


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  
engine.setProperty('rate', 150)

def talk(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("User:", command)
        return command.lower()
    except sr.UnknownValueError:
        talk("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        talk("Service is currently unavailable.")
        return ""

def run_assistant():
    talk("Hello, I'm your voice assistant. How can I help?")
    while True:
        command = listen_command()

        if 'play' in command:
            song = command.replace('play', '').strip()
            talk(f"Playing {song}")
            pywhatkit.playonyt(song)

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk(f"The current time is {time}")

        elif 'who is' in command:
            person = command.replace('who is', '').strip()
            info = wikipedia.summary(person, sentences=2)
            talk(info)

        elif 'open google' in command:
            webbrowser.open('https://www.google.com')
            talk("Opening Google")

        elif 'open youtube' in command:
            webbrowser.open('https://www.youtube.com')
            talk("Opening YouTube")

        elif 'exit' in command or 'stop' in command:
            talk("Goodbye!")
            break

        elif command:
            talk("I didn't understand that. Can you repeat?")

# Run the assistant
run_assistant()
