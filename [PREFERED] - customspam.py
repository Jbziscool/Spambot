import pyautogui
import time
from time import sleep

confirmation = True

ammount = input('Number to spam: ')
message = input('What msg: ')
if confirmation != False:
    confirmationvar = input('\nHave u clicked the textbox\nY to start: ').lower()
    print("\n")
    if confirmationvar not in['y', "yes"]:
        print("\n\nYou must type y or yes to agree.\n")
        exit()
time.sleep(5)
cvalue = 0


for i in range(int(ammount)):
    pyautogui.typewrite(message) 
    pyautogui.press('enter')
    cvalue+=1
    print(f"Sent the message {cvalue} / {ammount} times.")
