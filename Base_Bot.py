from time import sleep
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


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
