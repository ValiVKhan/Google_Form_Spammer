import time
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#Inputs

spam_count = int(275)
star_time = time.time()
repeat_count = 0

#Web Driving
try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
except:
    driver = webdriver.Firefox(executable_path=GeckoDriveManager().install())

#Opener

def opener():
    #Form Opening
    driver.get('https://typing-speed-test.aoeu.eu/')
    print("Form opened")
    time.sleep(1)
opener()

def reader():
    Box_1 = driver.find_element_by_css_selector('#currentword').text
    print(Box_1)
    type = driver.find_element_by_css_selector('#input')
    type.send_keys(Box_1," ")
    time.sleep(.05)



while (repeat_count<int(spam_count)):
    reader()
    repeat_count = repeat_count + 1


time.sleep(15)

driver.quit()


