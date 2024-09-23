import speech_recognition as sr  # For speech-to-text
import pyttsx3  # For text-to-speech (TTS)
import webbrowser  # For opening web pages
import datetime  # For fetching the current time
import os  # For interacting with the operating system (e.g., opening files)
import subprocess  # For running system commands

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """This function makes the system speak the given text."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """This function listens to voice input and returns recognized text."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for noise
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            # Using Google Web Speech API to recognize the voice input
            query = recognizer.recognize_google(audio)
            print(f"You said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not catch that. Could you repeat?")
            return None
        except sr.RequestError:
            speak("Sorry, the service is unavailable at the moment.")
            return None

def get_current_time():
    """Returns the current time as a string."""
    now = datetime.datetime.now()
    return now.strftime("%I:%M %p")

def open_notepad():
    """Opens Notepad (for Windows) or TextEdit (for macOS)."""
    if os.name == 'nt':  # Windows
        os.system("notepad")
    elif os.name == 'posix':  # macOS/Linux
        subprocess.run(["open", "-a", "TextEdit"])

def jarvis():
    """Main function for Jarvis to listen and respond to voice commands."""
    while True:
        command = listen()  # Listen for the user's command
        if command:
            if "hello" in command:
                speak("Hello, how can I assist you?")
            elif "what is your name" in command:
                speak("My name is Jarvis. I'm here to help you.")
            elif "open google" in command:
                speak("Opening Google")
                webbrowser.open("https://www.google.com")
            elif "what time is it" in command:
                current_time = get_current_time()
                speak(f"The time is {current_time}")
            elif "open notepad" in command:
                speak("Opening Notepad")
                open_notepad()
            elif "search for" in command:
                search_query = command.replace("search for", "").strip()
                speak(f"Searching for {search_query} on Google")
                webbrowser.open(f"https://www.google.com/search?q={search_query}")
            elif "play music" in command:
                music_dir = "C:\\Users\\YourUsername\\Music"  # Change to your music directory
                songs = os.listdir(music_dir)
                if songs:
                    os.startfile(os.path.join(music_dir, songs[0]))
                    speak("Playing music")
                else:
                    speak("No music files found in the directory.")
            elif "exit" in command or "goodbye" in command:
                speak("Goodbye!")
                break
            else:
                speak("I'm sorry, I don't recognize this command.")

if __name__ == "__main__":
    jarvis()
