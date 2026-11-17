# 🤖 Nova - AI Lab Virtual Assistant

A modular, voice-and-text-enabled Virtual Assistant built using Python. Designed specifically for AI Lab submissions, this project implements Speech Recognition, Intent Classification, Action Execution, and Offline Text-to-Speech (TTS).

---

## 📐 System Architecture

The virtual assistant pipeline operates through four modular stages designed for clear explanation during your academic lab viva:

1. **Speech-to-Text (STT):** Captures microphone audio input and utilizes the `SpeechRecognition` library to transcribe spoken phrases into a clean text string.
2. **Intent Recognition (The "Brain"):** Parses the transcribed text to identify user intent using rule-based keyword matching or an LLM API integration.
3. **Action Execution:** Triggers core Python backend functions to perform tasks such as opening desktop applications, fetching Wikipedia summaries, retrieving the current time, or searching the web.
4. **Text-to-Speech (TTS):** Converts the assistant's text-based response back into spoken audio using `pyttsx3` for seamless offline reliability.


---

## 🛠️ Prerequisites & Installation

### Step 1: Project Setup
Create a dedicated project folder on your system and open your terminal or command prompt inside that directory.

### Step 2: Install Required Libraries
Run the following command to install all necessary Python dependencies:


pip install SpeechRecognition pyttsx3 wikipedia pywhatkit pyaudio

## Troubleshooting Tips:
​If you encounter execution issues or permission warnings while running the installation or script, try running your terminal inside PowerShell.
​If your project expands to include a web frontend or user interface components, you can easily preview and run HTML files directly within VS Code using extensions like Live Server.
​## 🚀 Running the Application
​Execute the main Python script from your terminal or PowerShell:
python assistant.py

