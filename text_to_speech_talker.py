import win32api
import pyttsx3
import sys

tts = pyttsx3.init()

print("Text to Speech Talker")
print("\n")
print("Enter the text to speak, or QUIT to quit.")
while True:
    text = input(" ")
    if text.upper() == "QUIT":
        sys.exit()

    tts.say(text)
    tts.runAndWait()
