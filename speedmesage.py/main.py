import random
import pyautogui as pg 
import time
import keyboard

words = ("spam","spam")

time.sleep(5)   

for i in range(100):
    a = random.choice(words)
    pg.write(a)
    pg.press("enter")
        
    if keyboard.is_pressed("a"):
        break
