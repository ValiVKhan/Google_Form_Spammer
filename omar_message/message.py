from time import sleep
import pyautogui

sleep(2)

script = open('script.txt', 'r')

lines = script.readlines()

for line in lines:
    sleep(.5)
    if not line.strip():
            continue
    pyautogui.typewrite(line.strip())
    pyautogui.press('enter')
