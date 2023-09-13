import random
import pyautogui as pg 
import time
import keyboard

words = ("emre gaysin","gay")

time.sleep(5)   

for i in range(10000):
    a = random.choice(words)
    pg.write(a)
    pg.press("enter")
        
    if keyboard.is_pressed("a"):
        break
