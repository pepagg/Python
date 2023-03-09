from pyautogui import *
import pyautogui
import time
import keyboard


redcheck = None

for x in range(22):
 pyautogui.moveTo(1063, 52)
 pyautogui.dragTo(174, 52, button='left')  
 time.sleep(1)
 keyboard.press_and_release('ctrl+c')
 pyautogui.moveTo(268, 17)
 pyautogui.click() 
 pyautogui.moveTo(1063, 52)
 keyboard.press_and_release('ctrl+v')
 keyboard.press_and_release('enter')
 time.sleep(1)
 pyautogui.moveTo(804, 485)
 pyautogui.click()
 time.sleep(0.5)
 pyautogui.moveTo(468, 16)
 if pyautogui.pixel(804, 485)[0] in range(150, 233):
     redcheck = True
 else:
     redcheck = False
 pyautogui.click()
 if redcheck == False:
     pyautogui.moveTo(804, 485)
 else:
     pyautogui.moveTo(1029, 485)
 pyautogui.click() 
 pyautogui.moveTo(950, 700)
 pyautogui.click() 
