# You need to install speech recognition, datetime, pyttsx3, webbrowser, hugchat if you don't have these modules or packages priorly 
# And also along with this code you need to have a cookie file which should be in the format of .json and you can get it by adding cookie editor extension to your browser and can import cookies to use free api
# So this is a code for voice assistant and you can upgrade this code as your wish and your requirements
# Jarvis: Smart Voice Assistant with AI Chatbot

import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os
import json  # Add json module for error handling
from hugchat import hugchat, exceptions  # Import exceptions for better error handling
import time  # Import time for delays

# Initialize speech engine
speech = pyttsx3.init()
speech.say("Hello, I am Jarvis, your voice assistant, how can I help you?")
speech.runAndWait()

# Define the sites in a list
sites = [
    {"name": "YouTube", "url": "https://youtube.com"},
    {"name": "Google", "url": "https://google.com"},
    {"name": "Wikipedia", "url": "https://wikipedia.com"},
]

chatStr = ""

# Function to take command from the user
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        r.adjust_for_ambient_noise(source, duration=2)  # Increased duration for ambient noise
        print("Listening...")
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
        return query.lower()  # Convert to lowercase for easier comparison
    except sr.UnknownValueError:
        print("Could not understand audio.")
        speech.say("Sorry, I can't hear you. Please try again.")
        speech.runAndWait()
        return ""  # Return empty string if speech is not recognized
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service: {e}")
        return ""  # Return empty string if there is a request error

# Function to interact with the chatbot
def chatBot(query):
    if not query:  # Check for empty query
        return  # Don't proceed if there's no input

    try:
        user_input = query.lower()
        chatbot = hugchat.ChatBot(cookie_path=r"Feel free to add your file path of your cookies file")
        id = chatbot.new_conversation()
        chatbot.change_conversation(id)
        response = chatbot.chat(user_input)
        print(response)

        # Convert the response to a string (if it's not already)
        response_str = str(response)  # Ensure response is a string

        # Split the response into lines for processing
        response_lines = response_str.splitlines()
        
        # Speak the first four to five lines if there are more than four
        if len(response_lines) > 4:
            for line in response_lines[:5]:  # Speak the first five lines
                speech.say(line)
                speech.runAndWait()  # Wait for each line to finish before continuing
            
            # Inform the user that more content is available
            speech.say("The rest is below.")
            speech.runAndWait()

            time.sleep(5)  # Wait for 5 seconds before listening for more commands
            print("\n".join(response_lines[5:]))  # Print the remaining lines
        else:
            # If response is 4 lines or less, just read the whole response
            speech.say(response_str)
            speech.runAndWait()

    except exceptions.ChatError as e:
        print(f"Chatbot Error: {e}")
        speech.say("I'm sorry, there was an issue with the chatbot service.")
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        speech.say("There was an issue processing the response from the chatbot.")
    except Exception as e:
        print(f"Error: {e}")
        speech.say("Something went wrong, please try again.")
    speech.runAndWait()

# Main loop
while True:
    query = takeCommand()  # Capture command once

    # Check for specific commands first
    if "open" in query:
        opened = False  # To track if the app/site was opened

        # Open predefined sites
        for site in sites:
            if f"open {site['name'].lower()}" in query:
                speech.say(f"Opening {site['name']}, Sir...")
                speech.runAndWait()
                webbrowser.open(site["url"])
                opened = True
                break  # Exit the loop after opening the site

        # Open local applications using os.startfile
        if not opened:
            try:
                app_query = query.replace("open ", "").strip()
                os.startfile(app_query)
                speech.say(f"Opening {app_query}")
            except Exception as e:
                speech.say(f"Sorry, I couldn't open {app_query}. Please try again.")
                print(f"Error: {e}")
            speech.runAndWait()

    elif "the time" in query:
        hours = datetime.datetime.now().strftime("%H")
        mins = datetime.datetime.now().strftime("%M")
        speech.say(f"Sir, the time is {hours} {mins}.")
        speech.runAndWait()

    elif "the date" in query:  # Check if the user asks for the date
        today = datetime.datetime.now().strftime("%B %d, %Y")  # Format the date as "Month Day, Year"
        speech.say(f"Sir, today's date is {today}.")  # Announce the date
        speech.runAndWait()  # Wait for the speech to finish
        
    elif "jarvis quit" in query:
        speech.say("Goodbye, Sir!")
        speech.runAndWait()
        break  # Exit the loop

    elif "reset chat" in query:
        chatStr = ""
        speech.say("Chat has been reset.")
        speech.runAndWait()

    else:
        print("Searching....")
        chatBot(query)
