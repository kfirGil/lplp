import keyboard
from pyautogui import * 
import pyautogui 
import time
import win32api, win32con


def move1():
    pyautogui.hotkey('alt', 'TAB')

def check():

    flag = 0
    pic = pyautogui.screenshot(region=(100, 100, 1640, 900))

    width, height = pic.size

    for x in range(0, width, 5):
        for y in range(0, height, 5):

            r, g, b = pic.getpixel((x, y))

            if r == 166 and g == 208 and b == 175:
                flag = 1
                pyautogui.click(x+80, y+80)
                time.sleep(0.05)
                move1()
                break

        if flag == 1:
            break


while keyboard.is_pressed('q') == False:
    check()
    time.sleep(2)
   