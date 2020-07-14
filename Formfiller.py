import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Initiliaze Webdriver
try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
except:
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())


def opener():
    # Opening Form.
    driver.get('https://forms.gle/PuYwkSksWY48cUMh6')
    print ("Form Opened")
    time.sleep(2)

opener()

# User Input options
Option = input("What Option? ")


repeat_count = 0

def NameLogin():

    # Random Name Generator

    import random

    name1_number = (random.SystemRandom().randint(0, 284))
    name2_number = (random.SystemRandom().randint(0, 284))


    file_open = open('Texter.py')

    all_lines = file_open.readlines()

    random1_name = (all_lines[name1_number])
    random2_name = (all_lines[name2_number])


    #Entering Name
    Name_box = driver.find_element_by_css_selector('.freebirdFormviewerViewNumberedItemContainer:nth-child(1) .quantumWizTextinputPaperinputInput')
    Name_box.send_keys(random1_name)
    print(name1_number, ",", random1_name, 'inputed')
    time.sleep(1)


    #Entering Second Name
    Name2_box = driver.find_element_by_css_selector('.freebirdFormviewerViewNumberedItemContainer:nth-child(2) .quantumWizTextinputPaperinputInput')
    Name2_box.send_keys(random2_name)
    print(name2_number, ",", random2_name, 'inputed')
    time.sleep(1)

    if Option =="A":

        #Pressing The Options
        Options_box_A = driver.find_element_by_css_selector('.freebirdFormviewerComponentsQuestionRadioChoice:nth-child(1) .docssharedWizToggleLabeledLabelText')
        Options_box_A.click()
        print('Option A slected')
        time.sleep(2)

    if Option =="B":
        #Pressing The Options
        Options_box_B = driver.find_element_by_css_selector('.freebirdFormviewerComponentsQuestionRadioChoice:nth-child(2) .docssharedWizToggleLabeledLabelText')
        Options_box_B.click()
        print('Option B slected')
        time.sleep(2)

    #Pressing The Submit Button
    submit_box = driver.find_element_by_css_selector('.appsMaterialWizButtonPaperbuttonFilled .appsMaterialWizButtonPaperbuttonLabel')
    submit_box.click()
    print('Submitted')
    time.sleep(2)



    #Submiting Another Response
    submit_another_box = driver.find_element_by_link_text('Submit another response')
    submit_another_box.click()
    print ("Submitting another response")
    time.sleep(2)




while (repeat_count<1):
    repeat_count = repeat_count + 1
    NameLogin()


driver.quit()
print("Chrome Quit")