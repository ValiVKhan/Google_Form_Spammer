import time
import random
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

#UserInputs

spam_count = input("How many times? ")

#Varibale sets


start_time = time.time()
repeat_count = 0

def opener():
    # Initiliaze Webdriver
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
    except:
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    # Opening Form.
    driver.get('https://apps.gehealthcare.com/')
    print ("APP OPENED")
    time.sleep(2)

    #Generating Word
    name_search = (random.SystemRandom().randint(0, 3))

    file_open = open('GE_Search.py')

    all_lines = file_open.readlines()

    random_search = (all_lines[name_search])

    print(random_search)

    #Typing on site
    Search_Box = driver.find_element_by_css_selector('.textbox')
    Search_Box.send_keys(random_search)
    
    time.sleep(1)
        #Entering
    Search_Box.send_keys(Keys.RETURN)
    print ("ENTERED")
    
    time.sleep(1)
    
    #Quitting
    driver.quit()
    print("Chrome Quit")
    time.sleep(2)

while (repeat_count< int(spam_count)):
    repeat_count = repeat_count + 1
    opener()

print("Execution Time:", (time.time() - start_time))
print("SPAM COMPLETE")