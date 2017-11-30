import urllib
import urllib2
import random
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

name = random.choice(open('Names.txt').readlines())
password = name + "twitterbots1"


driver = webdriver.Firefox('/Users/cory/Desktop/TwitterBots/geckodriver')
#driver = webdriver.Chrome('/Users/cory/Desktop/TwitterBots/chromedriver')

# Google sign up address
driver.get("https://accounts.google.com/SignUp?continue=https%3A%2F%2Fwww.google.com%2F&hl=en")

# giving first name
firstName = driver.find_element_by_id('FirstName')
firstName.send_keys(name.rstrip())

randomNum = ""
tries = 0

while (tries < 5):
    randomNum += str(random.randint(0, 9))
    tries = tries + 1

# giving last name
lastName = driver.find_element_by_id('LastName')
lastName.send_keys('Smith')

# giving gmail address
gmailAddress = driver.find_element_by_id('GmailAddress')
gmailAddress.send_keys(name.rstrip() + randomNum.rstrip())

# giving password
password = driver.find_element_by_id('Passwd')
password.send_keys(name.rstrip() + "twitterbots1")

# giving password again
passwordAgain = driver.find_element_by_id('PasswdAgain')
passwordAgain.send_keys(name.rstrip() + "twitterbots1")

# clicking birth month
birthMonth = driver.find_elements_by_xpath('//*[@title="Birthday"]')[0]
birthMonth.click()

# clicking Augest month
birthMonth = driver.find_element_by_id(':8')
birthMonth.click()

# giving day
day = driver.find_element_by_id('BirthDay')
day.send_keys("27")

# giving year
year = driver.find_element_by_id('BirthYear')
year.send_keys("1998")

# clicking gender
genderButton = driver.find_elements_by_xpath('//*[@title="Gender"]')[0]
genderButton.click()

# clicking other gender
otherGender = driver.find_element_by_id(':g')
otherGender.click()

logins = name.rstrip() + randomNum.rstrip() + ":" + name.rstrip() + "twitterbots1"
f = open('Logins.txt','a')
f.write(logins + '\n')
f.close()

# clicking next step button
nextStepButton = driver.find_elements_by_xpath('//*[@class="g-button g-button-submit"]')[0]
nextStepButton.click()

# as of right now, when I try and login to the Gmail account
# it says it can not be found. Doing further research.

'''
driver.get("https://twitter.com/signup")

# Twitter name
twitterName = driver.find_element_by_id('full-name')
twitterName.send_keys(name.rstrip())

# Twitter email
twitterEmail = driver.find_element_by_id('email')
twitterEmail.send_keys(name.rstrip() + randomNum.rstrip())

# I have found out that Twitter flags all Temp mail services, so I
# am creating Gmail accounts instead.
'''
#driver.close()
