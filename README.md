# ai-LAB
​1. System Architecture
​The pipeline in four stages:
​1. Speech-to-Text (STT): Captures microphone audio and converts it into a text string (SpeechRecognition).
​2. Intent Recognition (The "Brain"): Parses the text to determine what the user wants (Rule-based keyword matching or an LLM API).
​3. Action Execution: Triggers Python functions (opening apps, fetching Wikipedia summaries, telling the time, searching the web).
​4. Text-to-Speech (TTS): Converts the assistant's text response back into spoken audio (pyttsx3 for offline reliability).
​2. Prerequisites & Installation
​Create a project folder and install the required libraries via your terminal:
pip install SpeechRecognition pyttsx3 wikipedia pywhatkit pyaudio
If problem running with run it in powershell.
And can run html file on vs code directly
