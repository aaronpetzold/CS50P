# --- say.py ---

# --- Using cowsay and text-to-speech (pyttsx3) ---
# Takes user input, prints an ASCII cow saying it, and speaks it aloud
"""
import cowsay
import pyttsx3

engine = pyttsx3.init()
this = input("What´s this? ")
cowsay.cow(this)
engine.say(this)
engine.runAndWait()
"""