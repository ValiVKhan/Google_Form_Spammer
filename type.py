import time
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#Inputs

start_time = time.time()

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


    global timer
    timer = driver.find_element_by_xpath('//*[@id="timer"]').text
    print(timer)


reader()
while (int(timer)<=int(60)):
    reader()


time.sleep(15)

driver.quit()
