from time import sleep
import pyautogui

sleep(2)


phrase = input("what is the phrase: ")
count = input("What is the spam count: ")
f = open('script.txt','w')
initial = 0
while int(initial) < int(count):
    f.write(str(phrase)+"\n")
    initial = initial+1
f.close()
sleep(5)
script = open('script.txt', 'r')

lines = script.readlines()

for line in lines:
    if not line.strip():
            continue
    pyautogui.typewrite(line.strip())
    pyautogui.press('enter')

