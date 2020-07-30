import time
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

#Question
spam_count = input("How many times? ")
start_time = time.time()
repeat_count = 0

# Initiliaze Webdriver
try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
except:
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())


#Form opener
def opener():
    # Opening Form.
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSduGL0lzXwipqYp9M-yVz7JtW4DXzKcBn-_u7DA3-E1eFeDDg/viewform')
    print ("Form Opened")
    time.sleep(2)
opener()

def submit():
    #Random Name Generator
    name_number = (random.SystemRandom().randint(0, 1003))
    file_open = open('texter.txt', 'r')

    all_lines = file_open.readlines()

    random_name = (all_lines[name_number])

    file_open.close()
    #Addint the @ for the mail
    at = (random.SystemRandom().randint(0, 5))

    mail_open = open('Mail.txt', 'r')

    mail_lines = mail_open.readlines()

    random_at = (mail_lines[at])

    mail_open.close()
    # Creating the random username
    username2 = (random.SystemRandom().randint(0,999))
    username_open = open('username.txt', 'r')

    username_lines = username_open.readlines()

    random_username2 = (username_lines[username2])
    #YouTube Link
    youtubelink_number = (random.SystemRandom().randint(0,100))
    YouTubeLink_Open = open ('YouTubeLink.txt', 'r')

    youtubelink_lines = YouTubeLink_Open.readlines()

    random_youtubelink = (youtubelink_lines[youtubelink_number])
    #Username for Twit
    q4link_number = (random.SystemRandom().randint(0,7))
    q4Link_Open = open ('Q4.txt', 'r')

    q4link_lines = q4Link_Open.readlines()

    random_q4link = (q4link_lines[q4link_number])
    #Qestion 7

    question_7 = (random.SystemRandom().randint(0,10))
    question7_open = open('Q7.txt', 'r')

    question7_lines = question7_open.readlines()

    random7 = (question7_lines[question_7])

    #Question 8
    question_8 = (random.SystemRandom().randint(0,10))
    question8_open = open('phone.txt', 'r')

    question8_lines = question8_open.readlines()

    random8 = (question8_lines[question_8])
    #A
    question_8a = (random.SystemRandom().randint(0,10))
    question8a_open = open('city.txt', 'r')

    question8a_lines = question8a_open.readlines()

    random8a = (question8a_lines[question_8a])
    #Date
    question_9 = (random.SystemRandom().randint(0,11))
    question9_open = open('Month.txt', 'r')

    question9_lines = question9_open.readlines()

    random9 = (question9_lines[question_9])
    # Date
    question_9a = (random.SystemRandom().randint(12, 37))
    question9a_open = open('Month.txt', 'r')

    question9a_lines = question9a_open.readlines()

    random9a = (question9a_lines[question_9a])
    # Date
    question_9b = (random.SystemRandom().randint(43, 97))
    question9b_open = open('Month.txt', 'r')

    question9b_lines = question9b_open.readlines()

    random9b = (question9b_lines[question_9b])
    #Jobs
    # Date
    question_11 = (random.SystemRandom().randint(0,15))
    question11_open = open('Jobs.txt', 'r')

    question11_lines = question11_open.readlines()

    random11 = (question11_lines[question_11])

    #Input Email

    Email_box = driver.find_element_by_css_selector('.freebirdFormviewerComponentsQuestionBaseRoot > div:nth-child(1) .quantumWizTextinputPaperinputInput')
    Email_box.send_keys(str(random_name)+str(random_at))
    print(str(random_name)+str(random_at))
    time.sleep(.1)

    #Q2
    Q2_box = driver.find_element_by_css_selector('.quantumWizTextinputPapertextareaInput')
    strname = str(random_name) + str(random_username2)
    Q2_box.send_keys(strname)
    Q2_box.send_keys("yes")
    print(strname)
    time.sleep(.1)

    #Q3
    Q3_box = driver.find_element_by_css_selector('div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(3) > div > div > div.freebirdFormviewerComponentsQuestionTextRoot > div > div.quantumWizTextinputPapertextareaMainContent.exportContent > div.quantumWizTextinputPapertextareaContentArea.exportContentArea > textarea')
    Q3_box.send_keys("https://www.youtube.com/channel/"+str(random_youtubelink))
    print("https://www.youtube.com/channel/" + str(random_youtubelink))
    Q3_box.send_keys("https://twitter.com/"+str(random_name))
    print("https://twitter.com/" +str(random_name))
    Q3_box.send_keys("https://instagram.com/"+str(random_name))
    print("https://instagram.com/" + str(random_name))
    time.sleep(.1)

    #Q4

    Q4_box = driver.find_element_by_css_selector('.freebirdFormviewerViewNumberedItemContainer:nth-child(4) .quantumWizTextinputPaperinputInput')
    Q4_box.send_keys(random_q4link)
    print(random_q4link)
    time.sleep(.1)

    #Q5
    Q5_box = driver.find_element_by_css_selector('div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(5) > div > div > div.freebirdFormviewerComponentsQuestionRadioRoot > div > div > span > div > div:nth-child('+str(random.SystemRandom().randint(1,9))+') > label > div > div.appsMaterialWizToggleRadiogroupElContainer.exportContainerEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled > div > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div')
    Q5_box.click()
    print("Clicked"+str((random.SystemRandom().randint(1,9))))
    time.sleep(.1)

    #Q6
    Q6_box = driver.find_element_by_css_selector('div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(6) > div > div > div.freebirdFormviewerComponentsQuestionRadioRoot > div > div > span > div > div:nth-child('+ str(random.SystemRandom().randint(1,2))+') > label > div > div.appsMaterialWizToggleRadiogroupElContainer.exportContainerEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled > div > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div')
    Q6_box.click()
    print("Clicked"+str(random.SystemRandom().randint(1,2)))
    time.sleep(.1)

    if random.SystemRandom().randint(1,2) == 2:
        Q7a_box = driver.find_element_by_css_selector('.freebirdFormviewerViewNumberedItemContainer:nth-child(7) .freebirdFormviewerComponentsQuestionRadioChoice:nth-child('+str(random.SystemRandom().randint(9,10))+') > .docssharedWizToggleLabeledContainer:nth-child(1)')
        print("Clicked" + str(random.SystemRandom().randint(9,10)))
        Q7a_box.click()
        print("Clicked" + str(random.SystemRandom().randint(9,10)))
        time.sleep(.1)
    else:
        Q7b_box = driver.find_element_by_css_selector('.freebirdFormviewerViewNumberedItemContainer:nth-child(7) .freebirdFormviewerComponentsQuestionRadioChoice:nth-child('+str(random.SystemRandom().randint(1,8))+') > .docssharedWizToggleLabeledContainer:nth-child(1)')
        Q7b_box.click()
        print("Clicked" + str(random.SystemRandom().randint(1,8)))
        time.sleep(.1)
    #Q7
    Q7_box = driver.find_element_by_css_selector('div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(8) > div > div > div.freebirdFormviewerComponentsQuestionTextRoot > div > div.quantumWizTextinputPapertextareaMainContent.exportContent > div.quantumWizTextinputPapertextareaContentArea.exportContentArea > textarea')
    Q7_box.send_keys(random7)
    print(strname)
    time.sleep(.1)
    #Q8
    Q8_box = driver.find_element_by_css_selector('.freebirdFormviewerViewNumberedItemContainer:nth-child(9) .quantumWizTextinputPaperinputInput')
    Q8_box.send_keys(random_name)
    Q8_box.send_keys(" ")
    Q8_box.send_keys(random8)
    Q8_box.send_keys(" ")
    Q8_box.send_keys(random8a)
    print(random_name, random8, random8a)
    time.sleep(.1)

    #Q9
    Q4_box = driver.find_element_by_css_selector('.freebirdFormviewerComponentsQuestionDateDateInputs .quantumWizTextinputPaperinputInput')
    Q4_box.send_keys(str(random9)+str(random9a)+str(random9b))
    print(str(random9)+str(random9a)+str(random9b))
    time.sleep(.1)
    #10
    Q4_box = driver.find_element_by_css_selector('div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(11) > div > div > div.freebirdFormviewerComponentsQuestionRadioRoot > div > div > span > div > div:nth-child('+str(random.SystemRandom().randint(1, 2))+') > label > div > div.appsMaterialWizToggleRadiogroupElContainer.exportContainerEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled > div > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div')
    Q4_box.click()
    print("Click")
    time.sleep(.1)
    #11
    Q4_box = driver.find_element_by_css_selector('div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(12) > div > div > div.freebirdFormviewerComponentsQuestionRadioRoot > div > div > span > div > div:nth-child(1) > label > div > div.appsMaterialWizToggleRadiogroupElContainer.exportContainerEl.docssharedWizToggleLabeledControl.freebirdThemedRadio.freebirdThemedRadioDarkerDisabled > div > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div')
    Q4_box.click()
    print("Click")
    time.sleep(.1)
    #12
    q4_box = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[13]/div/div/div[2]/div/div[1]/div[2]/textarea')
    q4_box.send_keys("No")
    print("No")
    time.sleep(.1)
    #Q13
    q4_box = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div[1]/div[2]/textarea')
    q4_box.send_keys(random11)
    print(random11)
    time.sleep(.3)
    #Submit
    q4_box = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    q4_box.click()
    print("Submitted")
    time.sleep(.1)
    #Submiting Another Response
    submit_another_box = driver.find_element_by_link_text('Submit another response')
    submit_another_box.click()
    print ("Submitting another response")
    time.sleep(.1)



while (repeat_count< int(spam_count)):
    repeat_count = repeat_count + 1
    print(repeat_count)
    submit()

driver.quit()
print("Chrome Quit")



