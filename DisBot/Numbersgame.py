import random
line_num = 1
def line():

    file_open = open('Distext.py')

    all_lines = file_open  . readlines()

    sentence =(all_lines[line_num])

    print (sentence)
