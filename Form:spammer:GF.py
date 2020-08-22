import time
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#Inputs

start_time = time.time()
spam_count = input("How man times? ")
num = 0
x = 0
wait = .1
#Web Driving
try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
except:
    driver = webdriver.Firefox(executable_path=GeckoDriveManager().install())

#Opener

def opener():
    #Form Opening
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdNQ0A-oo4M5wP0oLIu1i7_x0loSBF0EYWrqdxLxbeUEbJFpg/viewform')
    print("Form opened")
    time.sleep(3)

opener()

def runner():
    #name
    name_number = (random.SystemRandom().randint(0,999))
    file_open = open('counted.txt','r')

    nameall = file_open.readlines()

    random_name = (nameall[name_number])

    name = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    name.send_keys(random_name)
    time.sleep(wait)
    #Location
    location_number = (random.SystemRandom().randint(1000, 1080))
    file_open = open('counted.txt', 'r')

    locateall = file_open.readlines()

    random_locate = (locateall[location_number])

    location = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    location.send_keys(random_locate)
    time.sleep(wait)
    #age
    agepic = (random.SystemRandom().randint(1, 4))
    age = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div['+str(agepic)+']/label/div/div[1]/div/div[3]/div')
    age.click()
    time.sleep(wait)
    #Groups do I stan
    group_number = (random.SystemRandom().randint(1081, 1094))
    file_open = open('counted.txt', 'r')

    groupall = file_open.readlines()

    random_group = (groupall[group_number])

    groups = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea')
    groups.send_keys(random_group)
    time.sleep(wait)
    #nouns
    noun_number = (random.SystemRandom().randint(1095, 1100))
    file_open = open('counted.txt', 'r')

    nounall = file_open.readlines()

    noun_group = (nounall[noun_number])

    nouns = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
    nouns.send_keys(noun_group)
    time.sleep(wait)
    #hobby
    hobby_number = (random.SystemRandom().randint(1101, 1121))
    file_open = open('counted.txt', 'r')

    hobbyall = file_open.readlines()

    hobby_group = (hobbyall[hobby_number])
    hobby = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div[2]/textarea')
    hobby.send_keys(hobby_group)
    time.sleep(wait)

    #pinap

    pinap_num = (random.SystemRandom().randint(1,2))

    hobby = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div/span/div/div[' + str(pinap_num) +']/label/div/div[1]/div/div[3]/div')
    hobby.click()
    time.sleep(wait)

    #Love
    love_num = (random.SystemRandom().randint(1,2))

    hobby = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div['+str(love_num)+']/label/div/div[1]/div/div[3]/div')
    hobby.click()
    print(love_num)
    time.sleep(wait)

    #Clingy
    cling_number = (random.SystemRandom().randint(1122, 1131))
    file_open = open('counted.txt', 'r')

    clingall = file_open.readlines()

    cling_group = (clingall[cling_number])

    clingy = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[1]/input')
    clingy.send_keys(cling_group)

    #date
    question_9 = (random.SystemRandom().randint(1132,1143))
    question9_open = open('counted.txt', 'r')

    question9_lines = question9_open.readlines()

    random9 = (question9_lines[question_9])
    # Date
    question_9a = (random.SystemRandom().randint(1144, 1171))
    question9a_open = open('counted.txt', 'r')

    question9a_lines = question9a_open.readlines()

    random9a = (question9a_lines[question_9a])
    # Date
    question_9b = (random.SystemRandom().randint(1172, 1182))
    question9b_open = open('counted.txt', 'r')

    question9b_lines = question9b_open.readlines()

    random9b = (question9b_lines[question_9b])


    Q4_box = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
    Q4_box.send_keys(str(random9)+str(random9a)+str(random9b))
    time.sleep(wait)

    #last
    question_9c = (random.SystemRandom().randint(1183, 1184))
    question9c_open = open('counted.txt', 'r')

    question9c_lines = question9c_open.readlines()

    lastnum = (question9c_lines[question_9c])

    last = driver.find_element_by_xpath('//*[@id='+str(lastnum)+']/div[3]/div')
    last.click()
    time.sleep(wait)

    #Submit
    q4_box = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    q4_box.click()
    time.sleep(wait)
    #Submiting Another Response
    submit_another_box = driver.find_element_by_link_text('Submit another response')
    submit_another_box.click()
    time.sleep(wait)

while (int(x)<int(spam_count)):
    x = x + 1
    print(x)
    runner()





driver.quit()
