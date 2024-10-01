# Jarvis: Smart Voice Assistant with AI Chatbot
Jarvis is a voice-activated smart assistant designed to help you with common tasks like opening websites, telling the time, and answering general questions. It integrates speech recognition, text-to-speech synthesis, and a conversational AI chatbot to provide a hands-free experience.

# Features
Voice Commands: Jarvis listens to your voice commands and responds in real-time.
AI Chatbot Integration: Uses an AI-powered chatbot to answer complex queries.
Open Websites: Voice-activated commands to open popular websites like YouTube, Google, and Wikipedia.
Tell Time: Get the current time through a simple voice command.
Extendable: Easy to add more commands, websites, and functionality.
Interactive: If there are more than 5 lines in the chatbot's response, Jarvis will read the first 5 and print the rest for you to view.

# Requirements
Make sure you have the following Python packages installed:
pip install speechrecognition
pip install pyttsx3
pip install hugchat
pip install pyaudio  # Required for the microphone input

# How to Run
Clone this repository or download the code.
Ensure the required Python packages are installed.
Run the jarvis.py file in your terminal.
python jarvis.py

# Supported Commands
"Open YouTube": Opens YouTube in the browser.
"Open Google": Opens Google in the browser.
"Open Wikipedia": Opens Wikipedia in the browser.
"What's the time?": Announces the current time.
AI Queries: Ask general questions like "What is the capital of France?" or "Tell me a joke."

# Example Usage
User: What's the time?
Jarvis: Sir, the time is 14:35.

User: Open YouTube.
Jarvis: Opening YouTube, Sir...

User: Who is the president of the USA?
Jarvis: The president of the USA is Joe Biden. The rest is below.

# How It Works
Speech Recognition: Uses speech_recognition library to convert your speech to text.
Text-to-Speech: Utilizes pyttsx3 to speak responses back to you.
AI Chatbot: Integrated with Hugging Face's HugChat to handle general queries.
Web Interaction: Opens websites using Python's webbrowser module.

# File Structure
jarvis.py: The main Python script that runs the voice assistant.
cookies.json: Stores cookies needed for HugChat to function.
requirements.txt: Lists all necessary Python packages for this project.
Troubleshooting
Audio Issues: Make sure your microphone is properly set up and accessible.
Missing Packages: If some packages fail to install, ensure your Python version is up to date.

# Future Enhancements
Add more voice commands and integrate with other APIs.
Improve conversational abilities and response accuracy.
Support additional languages for speech recognition.

# License
This project is licensed under the MIT License. See the LICENSE file for more details.
