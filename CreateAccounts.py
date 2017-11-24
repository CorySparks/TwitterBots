import urllib
import urllib2
import random
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

name = random.choice(open('Names.txt').readlines())
password = name + "twitterbots1"


driver = webdriver.Chrome('/Users/cory/Desktop/PythonTwitterBot/chromedriver')

# Temp Mail address
driver.get("https://maildrop.cc/")

# Giving email name
emailInput = driver.find_element_by_id('nav-inbox')
print name
emailInput.send_keys(name)

# click submit button
submitButton = driver.find_elements_by_xpath('//*[@id="nav-form"]/button')[0]
submitButton.click()

Email = driver.find_element_by_id("mainaddr")

email = Email.text
print email

driver.close()
