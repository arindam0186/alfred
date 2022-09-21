import pyttsx3

engine = pyttsx3.init('sapi5')

def setEngineProperties(vol, rate, voice):
    engine.setProperty('rate', rate)
    engine.setProperty('volume', vol)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voice[voice].id)