# File Objects
import random

name_number = (random.SystemRandom().randint(0, 284))


file_open = open('Texter.py')

all_lines = file_open. readlines()

name = (all_lines[name_number])

print(name , name_number)



