import time
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

#UserInputs
#option = input("What Option? ")
#color = input("What Color? ")
spam_count = input("How many times? ")
#begin = input("")





# Initiliaze Webdriver
try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
except:
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())


# User Input options


start_time = time.time()
repeat_count = 0

def opener():
    # Opening Form.
    driver.get('https://forms.gle/PuYwkSksWY48cUMh6')
    print ("Form Opened")
    time.sleep(2)

opener()

def NameLogin():

    # Random Name Generator


    name1_number = (random.SystemRandom().randint(0, 1003))
    name2_number = (random.SystemRandom().randint(0, 1003))


    file_open = open('texter.txt', 'r')

    all_lines = file_open.readlines()

    random1_name = (all_lines[name1_number])
    random2_name = (all_lines[name2_number])


    #Entering Name
    Name_box = driver.find_element_by_css_selector('.freebirdFormviewerViewNumberedItemContainer:nth-child(1) .quantumWizTextinputPaperinputInput')
    Name_box.send_keys(random1_name)
    print(name1_number, ",", random1_name, 'inputed')
    time.sleep(.1)


    #Entering Second Name
    Name2_box = driver.find_element_by_css_selector('.freebirdFormviewerViewNumberedItemContainer:nth-child(2) .quantumWizTextinputPaperinputInput')
    Name2_box.send_keys(random2_name)
    print(name2_number, ",", random2_name, 'inputed')
    time.sleep(.1)
#Options

    option_num = (random.SystemRandom().randint(1, 2))

    if option_num == 1:

        #Pressing The Options
        Options_box_A = driver.find_element_by_css_selector('.freebirdFormviewerComponentsQuestionRadioChoice:nth-child(1) .docssharedWizToggleLabeledLabelText')
        Options_box_A.click()
        print('Option A slected')
        time.sleep(.1)

    if option_num == 2:
        #Pressing The Options
        Options_box_B = driver.find_element_by_css_selector('.freebirdFormviewerComponentsQuestionRadioChoice:nth-child(2) .docssharedWizToggleLabeledLabelText')
        Options_box_B.click()
        print('Option B slected')
        time.sleep(.1)
#Color choices

    color_num = (random.SystemRandom().randint(1, 3))

    print(color_num)

    if color_num == 1:
        Options_checkbox_Red = driver.find_element_by_css_selector('.freebirdFormviewerComponentsQuestionCheckboxChoice:nth-child(1) .docssharedWizToggleLabeledLabelText')
        Options_checkbox_Red.click()
        print('Red slected')
        time.sleep(.1)

    if color_num == 2:
        Options_checkbox_Yellow = driver.find_element_by_css_selector('.freebirdFormviewerComponentsQuestionCheckboxChoice:nth-child(2) .docssharedWizToggleLabeledLabelText')
        Options_checkbox_Yellow.click()
        print('Yellow slected')
        time.sleep(.1)

    if color_num == 3:
        Options_checkbox_Blue = driver.find_element_by_css_selector('.freebirdFormviewerComponentsQuestionCheckboxChoice:nth-child(3) .docssharedWizToggleLabeledLabelText')
        Options_checkbox_Blue.click()
        print('Blue slected')
        time.sleep(1)

    #Pressing The Submit Button
    submit_box = driver.find_element_by_css_selector('.appsMaterialWizButtonPaperbuttonFilled .appsMaterialWizButtonPaperbuttonLabel')
    submit_box.click()
    print('Submitted')
    time.sleep(.1)

    #SpamCounter
    print("Current Spam Count:", repeat_count)

    #Submiting Another Response
    submit_another_box = driver.find_element_by_link_text('Submit another response')
    submit_another_box.click()
    print ("Submitting another response")
    time.sleep(.1)






while (repeat_count< int(spam_count)):
    repeat_count = repeat_count + 1
    NameLogin()


driver.quit()
print("Chrome Quit")
print("Total Spam Count:", spam_count)
#print("Selected Option:", option)
print("Execution Time:", (time.time() - start_time))
print("SPAM COMPLETE")