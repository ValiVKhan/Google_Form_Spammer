import time
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Inputs

spam_count = input("Spam count? ")
star_time = time.time()
repeat_count = 0

x = 0

# Web Driving
try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
except:
    driver = webdriver.Firefox(executable_path=GeckoDriveManager().install())


# Opener

def opener():
    # Form Opening
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdtNbL6WGGmsQCGH9pWIlO7fDk41P48Z_3GYk2mtqDuHVBr6A/viewform')
    print("Form opened")
    time.sleep(1)

opener()

def signer():

    prompt_number = (random.SystemRandom().randint(0,999))
    file_open = open("counted.txt",'r')
    all_lines = file_open.readlines()

    random_prompt =(all_lines[prompt_number])

    Box_1 = driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div['+str(random.SystemRandom().randint(1,6))+']/label/div/div[1]/div[2]')
    Box_1.click()
    #print("Clicked")
    time.sleep(x)

    Box_2 =driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea')
    Box_2.send_keys(random_prompt)
    #print(random_prompt)
    time.sleep(x)


    Box_3 =driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div['+str(random.SystemRandom().randint(1,4))+']/label/div/div[1]/div/div[3]/div')
    Box_3.click()
    #print("Clicked")
    time.sleep(x)


    Box_3 =driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div['+str(random.SystemRandom().randint(1,5))+']/label/div/div[1]/div/div[3]/div')
    Box_3.click()
    #print("Clicked")
    time.sleep(x)

    #Submit
    q4_box = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div/span/span')
    q4_box.click()
    #print("Submitted")
    time.sleep(x)

    #Submiting Another Response
    submit_another_box = driver.find_element_by_link_text('Submit another response')
    submit_another_box.click()
    #print ("Submitting another response")
    time.sleep(x)

while (repeat_count<int(spam_count)):
    repeat_count = repeat_count + 1
    print(repeat_count)
    signer()

driver.quit()