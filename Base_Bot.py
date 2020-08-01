import time
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#Inputs

#spam_count = input("How many times? ")
star_time = time.time()
spam_count = input("Spam count? ")
repeat_count = 0

#Web Driving
try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
except:
    driver = webdriver.Firefox(executable_path=GeckoDriveManager().install())

#Opener

def opener():
    #Form Opening
    driver.get('###############################################################')
    print("Form opened")
    time.sleep(1)
opener()


driver.quit()


