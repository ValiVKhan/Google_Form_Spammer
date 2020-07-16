import time
import random
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
#Inputs
spam_count = input("Spam count: ")

spam_count = 2 * spam_count

if int(spam_count) > 328:
    spam_count = 328
    print("Count too high, spam count set to 328")


# Initiliaze Webdriver
try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
except:
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())


# UserInputs


# Varibale sets
line_num = 1

start_time = time.time()
repeat_count = 0

def login():
    # Opening Form.
    driver.get('https://discord.com/login')
    print ("DISCORD OPENED")
    time.sleep(2)



    # Typing on site
    Email_Box = driver.find_element_by_name('email')
    Email_Box.send_keys("Email")

    Password_Box = driver.find_element_by_name('password')
    Password_Box.send_keys("Password")
    time.sleep(.5)
    # Entering
    Password_Box.send_keys(Keys.RETURN)
    print ("ENTERED")
    time.sleep(10)

    #Discord Chat
    #Over_Mes = driver.find_element_by_css_selector('#private-channels-2 .wrapper-3t9DeA')
    #ActionChains(driver).move_to_element(Over_Mes).perform()
    #time.sleep(1)
    Message_Box = driver.find_element_by_css_selector('#private-channels-2 .nameAndDecorators-5FJ2dg')
    Message_Box.click()
    time.sleep(5)

login()

def writer():
     #Generating Word
     file_open = open('Demo.txt')

     all_lines = file_open.readlines()

     sentence = (all_lines[line_num])

     print (sentence)
     print (int(line_num)-1)



     # Texter
     Text_Box = driver.find_element_by_css_selector('.markup-2BOw-j > div')
     Text_Box.send_keys(sentence)
     time.sleep(.3)
     Enter_Box = driver.find_element_by_css_selector('.markup-2BOw-j > div')
     Enter_Box.send_keys(Keys.RETURN)
     time.sleep(1)

while (line_num < int(spam_count)):
    writer()
    line_num = line_num + 2
    
driver.quit()
print("Chrome Quit")
print("Execution Time:", (time.time() - start_time))
print("SPAM COMPLETE")