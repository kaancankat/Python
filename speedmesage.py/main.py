import random
import pyautogui as pg 
import time
import pyautogui 

words = ("enayi","emre","agla","lolcu","hayatsiz")

time.sleep(3)   

for i in range(20):
    a = random.choice(words)
    pg.write("sen"  " "  + a)
    pg.press("enter")
    
    if pyautogui.press("esc"):
        
    
    