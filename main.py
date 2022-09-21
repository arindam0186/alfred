import speech_recognition as sr
from playsound import playsound
from tkinter import *
from decouple import config
from service.createJira import createJira

import pyttsx3

engine = pyttsx3.init('sapi5')

def setEngineProperties(vol, rate, voice):
    engine.setProperty('rate', rate)
    engine.setProperty('volume', vol)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice].id)

user = config('user')
virtual_assistant = config('virtual_assistant')

#text to speech conversion

def speak(text):
    engine.say(text)
    print(virtual_assistant + " : " + text)
    engine.runAndWait()

setEngineProperties(1.0, 200, 0)

def take_user_input():
    r = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:

        playsound("assistant_on.wav")
        print('Listening...')
        audio = r.listen(source)
        playsound("assistant_off.wav")
        print('Processing...')

    try:
        text = r.recognize_google(audio, language='en-in')
        print('You: ' + ': ' + text)
        return text

    except:
        return "None"

def processAudio():
    run = 1

    if __name__ == '__main__':
        while run==1:
            query = take_user_input().lower()
            results = ''
            run+=1

            if 'jira' in query:
                speak('Creating a jira, what is the JIRA summary?')
                summary=take_user_input().capitalize()
                speak('Summary noted, please state jira description')
                description=take_user_input().capitalize()
                createJira(summary,description)

def main_screen():

    global screen
    screen = Tk()
    screen.title(virtual_assistant)
    screen.geometry("100x250")
    screen.iconbitmap('artificial-intelligence-icon-1.png')


    name_label = Label(text = virtual_assistant,width = 300, bg = "black", fg="white", font = ("Calibri", 13))
    name_label.pack()


    microphone_photo = PhotoImage(file = "artificial-intelligence-icon-1.png")
    microphone_button = Button(image=microphone_photo, command = processAudio)
    microphone_button.pack(pady=10)

    screen.mainloop()


main_screen()