from voiceEngine import engine
from configBuilder import virtual_assistant

#text to speech conversion

def speak(text):
    engine.say(text)
    print(virtual_assistant + " : " + text)
    engine.runAndWait()