# Speech Recognition project for optimization with python
# by TAB Zakaria

import speech_recognition as sr
from gtts import gTTS
from pygame import mixer 
import os
import webbrowser
import re
import sys
import datetime

def TalkToMe(audio):
    print (audio)
    tts = gTTS(text=audio, lang='en')
    tts.save('audio.mp3')
    mixer.init()
    mixer.music.load('audio.mp3')
    mixer.music.play()

def MyCommands():
    r=sr.Recognizer()
    with sr.Microphone() as source:
         print ('speak:')
         r.adjust_for_ambient_noise(source,duration=1)
         audio = r.listen(source)
             
    try:
       command = r.recognize_google(audio)
       print ("you said : " + command + "\n")
    #loop back
    except sr.UnknownValueError:
           print('could not understand audio') 
           command = MyCommands()
    return command

def respond(command):

    if 'open Google' in command:
       url = 'http://www.google.com/'
       webbrowser.open_new_tab(url)
       print ('Google is ready !!')
    elif 'open YouTube' in command:
       url = 'https://www.youtube.com/'
       webbrowser.open_new_tab(url)
       print ('Youtube is ready !!')
    elif 'check my email' in command:
       url = 'https://mail.google.com/mail/u/0/#inbox'
       webbrowser.open_new_tab(url)
       print ('Gmail is ready !!')
    elif 'open Facebook' in command:
       url = 'https://www.facebook.com/'
       webbrowser.open_new_tab(url)
       print ('Facebook is ready !!')
                           
    elif 'who are you' in command :
       TalkToMe("I am zaki's desktop assistant ")
    elif 'what is your name'in command :
       TalkToMe('Rolla')
    elif 'can you hack'in command :
       TalkToMe("Haha , no i can't")
    elif 'hello' in command :
       TalkToMe('Hello , can i help you ?')
    elif 'thank you' in command :
       TalkToMe("you are welcome ")
    elif 'what time it is' in command :
         print (datetime.datetime.now())
    elif 'close program' in command:
         sys.exit(0)

while True:
      respond(MyCommands())
                  

               

           





