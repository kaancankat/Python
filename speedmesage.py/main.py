import random
import pyautogui as pg 
import time
import pyautogui 

words = ("okul diyen dayi","okula 7 gün var")

time.sleep(8)   

for i in range(20):
    a = random.choice(words)
    pg.write(a)
    pg.press("enter")
        
   #if pyautogui.press("esc"):
       