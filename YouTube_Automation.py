# ==========================================
# Script Name: YouTube_Automation.py
# Author: Dhiraj Kumar
# Date & Time: Saturday, June 27, 2026, at 2:16:12 PM IST
# Location: Hyderabad, Telangana, India
# Description: A Voice-controlled YouTube Assistant
#
# REQUIRED INSTALLATIONS:
# Please open your terminal or command prompt and run the following command 
# before running this script:
#
# pip install SpeechRecognition pyttsx3 pywhatkit pyaudio
# ==========================================

import speech_recognition as sr
import pyttsx3
import pywhatkit
import webbrowser
import time

# ==========================================
# 1. Initialize Text-to-Speech Engine
# ==========================================
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# Set to a female voice (usually index 1), or change to 0 for a male voice
engine.setProperty('voice', voices[1].id) 
engine.setProperty('rate', 160) # Speaking speed

def speak(text):
    """Makes the assistant speak out loud."""
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

# ==========================================
# 2. Voice Recognition Function
# ==========================================
def take_command():
    """Listens to the microphone and returns the recognized text."""
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening for a command...")
        listener.adjust_for_ambient_noise(source, duration=1)
        audio = listener.listen(source)

    try:
        command = listener.recognize_google(audio).lower()
        print(f"You said: '{command}'")
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        print("Could not request results; check your internet connection.")
        return ""

# ==========================================
# 3. YouTube Automation Logic
# ==========================================
def execute_youtube_command(command):
    """Parses the voice command and executes the corresponding YouTube action."""
    
    # Feature 1: Open YouTube
    if command == "open youtube":
        speak("Opening YouTube home page.")
        webbrowser.open("https://www.youtube.com")

    # Feature 2: Search YouTube
    elif "search youtube for" in command:
        search_query = command.replace("search youtube for", "").strip()
        speak(f"Searching YouTube for {search_query}.")
        webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")

    # Feature 3 & 4: Play videos / Play music
    elif "play video" in command or "play music" in command:
        # Strip the trigger words to isolate the song/video name
        media_query = command.replace("play video", "").replace("play music", "").replace("play", "").strip()
        speak(f"Playing {media_query} on YouTube.")
        # pywhatkit automatically finds the best match and plays it immediately
        pywhatkit.playonyt(media_query)

    # Feature 5: Open channel
    elif "open channel" in command:
        channel_name = command.replace("open channel", "").strip()
        # Remove spaces to format it as a YouTube handle (e.g., @mkbhd)
        formatted_channel = channel_name.replace(" ", "")
        speak(f"Opening the channel for {channel_name}.")
        webbrowser.open(f"https://www.youtube.com/@{formatted_channel}")

    # Feature 6: Open playlist
    elif "open playlist" in command or "open my playlist" in command:
        speak("Opening your YouTube playlists.")
        # Opens the URL where saved playlists live (requires you to be logged into your browser)
        webbrowser.open("https://www.youtube.com/feed/playlists")

    # Feature 7: Subscribe shortcut
    elif "subscribe" in command:
        speak("I cannot click the subscribe button directly for security reasons, but if you are on a video page, you can press the Tab key until Subscribe is highlighted, then press Enter!")
        
    # Exit command
    elif "exit" in command or "stop" in command:
        speak("Shutting down YouTube assistant. Goodbye, Dhiraj!")
        return False
        
    else:
        speak("I didn't recognize a YouTube command. Try saying 'Play music' or 'Search YouTube for'.")

    return True

# ==========================================
# 4. Main Loop
# ==========================================
if __name__ == "__main__":
    speak("YouTube Automation Assistant is online. What would you like to do, Dhiraj?")
    
    running = True
    while running:
        user_command = take_command()
        
        if user_command:
            running = execute_youtube_command(user_command)
        
        # Slight pause before listening again to prevent echoing
        time.sleep(1)
