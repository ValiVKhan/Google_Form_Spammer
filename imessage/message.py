from time import sleep
import pyautogui

sleep(2)


x = 0

while (x <99):
    script = open('script.txt', 'r')

    lines = script.readlines()

    print(lines)
    x = x + 1
    for line in lines:
        if not line.strip():
            continue
        pyautogui.typewrite(line.strip())
        pyautogui.press('enter')
