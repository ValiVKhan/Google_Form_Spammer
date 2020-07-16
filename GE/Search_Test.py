import random


name_search = (random.SystemRandom().randint(0, 3))

file_open = open('GE_Search.py')

print(name_search)

all_lines = file_open.readlines()

random_search = (all_lines[name_search])

print(random_search)