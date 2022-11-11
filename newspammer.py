haveready = input("Make sure you have your window ready that you want to spam\nIf you do type y: ")

if haveready not in["yes", "y"]:
    exit()

import pyautogui
import time
from time import sleep

time.sleep(4.6)
messagee = open('msg.txt')
notbeemovie = open('nobeemovie.txt')
cvalue = 0
nvalue = 0


pyautogui.typewrite('Someone doesnt like you time and has requested me to spam you goodbye!')
pyautogui.press('enter')
sleep(0.7) #remove this if you want
pyautogui.typewrite('----------------------------------')
pyautogui.press('enter')

for line in messagee:
    pyautogui.typewrite((line))
    pyautogui.press('enter')

    cvalue += 1
    print(f'Sent {cvalue} messages/2676')
