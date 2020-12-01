# auto type 
# using pynput
# first we have to install and import the modules 
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
time.sleep(2)
#here we use "for" loop to get repeated
for char in "THIS TIME I GOT THE ANSWER FULL HEADACHE":
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(0.15)



# using pyautogui

import pyautogui
import time

time.sleep(2)
pyautogui.typewrite('this is second trail',interval=0.25)
