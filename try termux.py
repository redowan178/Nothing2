import pyttsx3
import os
os.system('pip install pyttsx3')

text = "Hello, this is a text-to-speech example."
engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()