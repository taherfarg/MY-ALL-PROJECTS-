import speech_recognition as sr
import time

# Create a recognizer object
r = sr.Recognizer()

# Use the default microphone as the audio source
with sr.Microphone() as source:
    print("Speak now!")
    # Adjust for ambient noise
    r.adjust_for_ambient_noise(source)
    # Listen for audio and convert it to text
    audio = r.listen(source, timeout=30, phrase_time_limit=10)

    try:
        # Recognize the speech in the audio
        text = r.recognize_google(audio, language=['en-US', 'ar-SA'])
        print(f"You said: {text}")

        # Save the text to a file
        with open('speech-to-text.txt', 'w') as file:
            file.write(text)
            print("Text saved to file.")
    except sr.UnknownValueError:
        print("Sorry, I didn't understand what you said.")
    except sr.RequestError:
        print("Sorry, speech recognition is not available at the moment.")
