# File Objects
import random

name_number = (random.SystemRandom().randint(0, 500))


file_open = open('Texter.txt','r')

all_lines = file_open. readlines()

name = (all_lines[name_number])

print(name)

if name_number == 3:
    print("red")



