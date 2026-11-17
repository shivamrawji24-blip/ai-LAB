import speech_recognition as sr
import pyttsx3
import sounddevice as sd
import scipy.io.wavfile as wav
import datetime
import wikipedia
import webbrowser
import tempfile
import os

# Initialize offline Text-to-Speech
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id if len(voices) > 1 else voices[0].id)
engine.setProperty('rate', 175)

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def greet_user():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Nova, your AI lab assistant. How can I help you?")

def listen_command(use_mic=True, duration=5, fs=16000):
    if not use_mic:
        return input("You (Type command): ").lower()

    print(f"\nListening ({duration}s)...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    print("Recognizing...")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
        wav.write(tmp_file.name, fs, recording)
        tmp_path = tmp_file.name

    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(tmp_path) as source:
            audio = recognizer.record(source)
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"You: {query}")
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Could you repeat?")
        return ""
    except sr.RequestError:
        speak("Network error. Switching to text input.")
        return input("You (Type command): ").lower()
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)

def process_command(query):
    if not query:
        return True

    if 'wikipedia' in query or 'who is' in query or 'what is' in query:
        speak("Searching Wikipedia...")
        topic = query.replace("wikipedia", "").replace("who is", "").replace("what is", "").strip()
        try:
            results = wikipedia.summary(topic, sentences=2)
            speak("According to Wikipedia:")
            speak(results)
        except Exception:
            speak("I couldn't find clear information on that topic.")

    elif 'time' in query:
        speak(f"The current time is {datetime.datetime.now().strftime('%I:%M %p')}")

    elif 'date' in query:
        speak(f"Today's date is {datetime.datetime.now().strftime('%B %d, %Y')}")

    elif 'open youtube' in query:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    elif 'open google' in query:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")

    elif 'search' in query:
        search_term = query.replace("search", "").strip()
        speak(f"Searching Google for {search_term}")
        webbrowser.open(f"https://www.google.com/search?q={search_term}")

    elif 'open calculator' in query:
        speak("Opening Calculator.")
        os.system("calc")

    elif 'exit' in query or 'stop' in query or 'bye' in query:
        speak("Shutting down. Good luck with your AI lab!")
        return False

    else:
        speak("Searching Google for that.")
        webbrowser.open(f"https://www.google.com/search?q={query}")

    return True

if __name__ == "__main__":
    greet_user()
    running = True
    while running:
        user_query = listen_command(use_mic=True)
        running = process_command(user_query)