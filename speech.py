import speech_recognition as sr
import time
import sys

# create a recognizer object
r = sr.Recognizer()

# use the default microphone as the audio source
with sr.Microphone() as source:
    print("Say something!")
    # adjust for ambient noise levels
    r.adjust_for_ambient_noise(source)

    # listen for 30 seconds
    audio = r.listen(source, phrase_time_limit=30)

    print("Transcribing...")

    # recognize speech using Google Speech Recognition
    try:
        text = r.recognize_google(audio, language='ar-EG,en-US')
        print(f"You said: {text}")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        
    # wait for 30 seconds before ending the program
    time.sleep(30)
