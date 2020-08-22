import time
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#Inputs

start_time = time.time()
word_count = 1
num = 0
x = 0
#Web Driving
try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
except:
    driver = webdriver.Firefox(executable_path=GeckoDriveManager().install())

#Opener

def opener():
    #Form Opening
    driver.get('https://www.typingtest.com/')
    print("Form opened")
    time.sleep(3)

opener()
def player():
    start = driver.find_element_by_xpath('//*[@id="testStartForm"]/button')
    start.click()
    time.sleep(3)

player()
def reader():
    Box_1 = driver.find_element_by_xpath('//*[@id="test-container"]/div[2]/span[' + str(num) + ']').text
    print(Box_1)

    type = driver.find_element_by_xpath('//*[@id="test-edit-area"]')
    type.send_keys(Box_1," ")



while num < 10000:
    num = num + 1
    reader()
time.sleep(5)


driver.quit()
