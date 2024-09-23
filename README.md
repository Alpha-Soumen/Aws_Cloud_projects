# Jarvis - Your Personal Voice Assistant

![Jarvis Logo](https://github.com/yourusername/jarvis/blob/main/assets/jarvis-logo.png)

**Jarvis** is a Python-based voice assistant that can understand and execute basic voice commands. Enhance your productivity by interacting with your computer hands-free! This project uses speech recognition and text-to-speech libraries to provide a seamless voice-controlled experience.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Voice Recognition:** Understands and processes voice commands.
- **Text-to-Speech:** Responds with spoken words.
- **Web Interaction:** Open websites and perform Google searches.
- **System Operations:** Open applications like Notepad/TextEdit.
- **Time Inquiry:** Tells the current time.
- **Music Playback:** Plays music from a specified directory.
- **Exit Commands:** Gracefully terminate the program with voice commands.

## Installation

### Prerequisites

- **Python 3.6+**: Ensure Python is installed on your system. [Download Python](https://www.python.org/downloads/)
- **Pip**: Python package manager. Usually comes with Python installation.

### Clone the Repository

```bash
git clone https://github.com/yourusername/jarvis.git
cd jarvis
```

### Install Dependencies

It's recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

**`requirements.txt`**:
```plaintext
speechrecognition
pyttsx3
pyaudio
```

*Note: For Windows users, installing `pyaudio` might require downloading the appropriate wheel file from [PyAudio Downloads](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and installing it via `pip install your_downloaded_whl_file`.*

## Usage

Run the Jarvis program using Python:

```bash
python jarvis.py
```

Jarvis will start listening for your voice commands. Speak clearly into your microphone to interact.

## Commands

Here are the basic commands you can use with Jarvis:

### 1. Tell the Current Time

- **Command:** "What time is it?"
- **Response:** Jarvis will announce the current time.

### 2. Open Notepad/TextEdit

- **Command:** "Open Notepad"
- **Response:** Jarvis will open Notepad on Windows or TextEdit on macOS.

### 3. Search the Web

- **Command:** "Search for [something]"
- **Response:** Jarvis will perform a Google search for the specified query.

### 4. Play Music

- **Command:** "Play music"
- **Response:** Jarvis will play the first song in the specified music directory.

### 5. Exit the Program

- **Command:** "Exit" or "Goodbye"
- **Response:** Jarvis will say goodbye and terminate the program.

### Example Interaction

```plaintext
You: Hello
Jarvis: Hello, how can I assist you?

You: What time is it?
Jarvis: The time is 03:45 PM.

You: Open Google
Jarvis: Opening Google.

You: Play music
Jarvis: Playing music.

You: Goodbye
Jarvis: Goodbye!
```

## Code Overview

Here's the enhanced version of the Jarvis program with additional basic commands:

```python
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
```

### Added Commands

1. **Tell the Current Time:**
   - **Command:** "What time is it?"
   - **Response:** Jarvis will speak the current time using the `get_current_time()` function.

2. **Open Notepad/TextEdit:**
   - **Command:** "Open Notepad"
   - **Response:** Jarvis will open Notepad on Windows or TextEdit on macOS using the `open_notepad()` function.

3. **Search the Web:**
   - **Command:** "Search for [something]"
   - **Response:** Jarvis will perform a Google search for the specified query.

4. **Play Music:**
   - **Command:** "Play music"
   - **Response:** Jarvis will play the first song in the specified music directory (`music_dir`). You need to adjust the path to your music folder.

5. **Exit the Program:**
   - **Command:** "Exit" or "Goodbye"
   - **Response:** Jarvis will say goodbye and terminate the program.

## Customization

### Adding More Commands

You can expand Jarvis's capabilities by adding more commands. To do this, modify the `jarvis()` function by adding additional `elif` blocks. For example:

```python
elif "tell me a joke" in command:
    speak("Why did the computer show up at work late? It had a hard drive!")
```

### Updating Music Directory

Ensure you update the `music_dir` variable with the correct path to your music files:

```python
music_dir = "C:\\Users\\YourUsername\\Music"  # Windows
# or
music_dir = "/Users/YourUsername/Music"  # macOS/Linux
```

### Improving Voice Recognition

For better accuracy, consider using more advanced speech recognition services or models. You can integrate APIs like [Wit.ai](https://wit.ai/) or [IBM Watson](https://www.ibm.com/watson) for enhanced capabilities.

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the repository**
2. **Create a new branch** (`git checkout -b feature/YourFeature`)
3. **Commit your changes** (`git commit -m 'Add some feature'`)
4. **Push to the branch** (`git push origin feature/YourFeature`)
5. **Open a Pull Request**

Please ensure your code follows the project's coding standards and includes relevant documentation.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to customize and enhance Jarvis to better suit your needs. Happy coding!
