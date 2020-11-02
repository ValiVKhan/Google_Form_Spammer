from time import sleep
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

#Question
#spam_count = input("How many times? ")
#start_time = time.time()
repeat_count = 0

# Initiliaze Webdriver
try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
except:
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())


#Form opener
def opener():
    # Opening Form.
    driver.get('https://www.donaldjtrump.com/landing/2020-trump-vs-dem-poll')
    print ("Form Opened")
    sleep(2)
opener()

x = 0
def survey():

    question = driver.find_element_by_xpath('//*[@id="fields[340]-1"]')
    question.click()


    question = driver.find_element_by_xpath('//*[@id="fields[341]-1"]')
    question.click()

    question = driver.find_element_by_xpath('//*[@id="fields[342]-1"]')
    question.click()

    question = driver.find_element_by_xpath('//*[@id="fields[343]-1"]')
    question.click()

    question = driver.find_element_by_xpath('//*[@id="fields[344]-1"]')
    question.click()

    question = driver.find_element_by_xpath('//*[@id="fields[345]-1"]')
    question.click()

    question = driver.find_element_by_xpath('//*[@id="fields[346]-1"]')
    question.click()

    question = driver.find_element_by_xpath('//*[@id="fields[347]-1"]')
    question.click()

    question = driver.find_element_by_xpath('//*[@id="fields[348]-1"]')
    question.click()

    question = driver.find_element_by_xpath('//*[@id="fields[411]-1"]')
    question.click()

    question1 = driver.find_element_by_xpath('//*[@id="fields[411]-1"]')
    question1.click()

    name_number = (random.SystemRandom().randint(5003, 8008))
    file_open = open('info.txt', 'r')

    all_lines = file_open.readlines()

    random_name = (all_lines[name_number])

    question = driver.find_element_by_xpath('//*[@id="ddform_350"]')
    question.send_keys(random_name)

    last_number = (random.SystemRandom().randint(8010, 8291))
    file_open = open('info.txt', 'r')

    all_lines = file_open.readlines()

    last_name = (all_lines[last_number])

    question = driver.find_element_by_xpath('//*[@id="ddform_351"]')
    question.send_keys(last_name)


    mail2_number = (random.SystemRandom().randint(8293, 8296))
    file_open = open('info.txt', 'r')

    all_lines = file_open.readlines()

    mail2_name = (all_lines[mail2_number])

    question = driver.find_element_by_xpath('//*[@id="ddform_352"]')
    question.send_keys((random_name)+(last_name)+(mail2_name))
    
    zip_number = (random.SystemRandom().randint(0, 5000))
    file_open = open('info.txt', 'r')

    all_lines = file_open.readlines()

    zip_name = (all_lines[zip_number])
    question = driver.find_element_by_xpath('//*[@id="ddform_353"]')
    question.send_keys(zip_name)





while 1:
    survey()
    x = x + 1
    print(x)
    opener()
