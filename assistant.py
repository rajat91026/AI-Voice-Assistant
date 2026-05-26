import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import wikipedia

engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except Exception as e:
        print(e)
        speak("Sorry, I did not understand.")
        return ""

speak("Hello Rajat, I am your AI assistant.")

while True:
    command = take_command()

    if "youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    elif "google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")

    elif "wikipedia" in command:
        speak("What should I search?")
        query = take_command()

        try:
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        except:
            speak("No result found.")

    elif "exit" in command:
        speak("Goodbye")
        break