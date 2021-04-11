# Imports
import os
import time
import pystray
import speech_recognition as sr
from PIL import Image
from pystray import Menu, MenuItem

# Voice Recognition
def callback(recognizer, audio):
    try:
        if(recognizer.recognize(audio) == "Python shut down PC" or recognizer.recognize(audio) == "Python shutdown PC" ):
            os.system("shutdown /s /t 0")
    except LookupError:
        pass
        
r = sr.Recognizer()
r.listen_in_background(sr.Microphone(), callback)

# Kill
def exit_action(icon):
    icon.visible = False
    icon.stop()
    quit()

# Tray icon
def init_icon():
    icon = pystray.Icon('pc-off',)
    icon.menu = Menu(MenuItem('Exit', lambda : exit_action(icon)),)
    icon.icon = Image.open('icon.ico')
    icon.title = 'pc-off'

    icon.run()

init_icon()

while True: time.sleep(0.1)