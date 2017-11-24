import urllib
import urllib2
import random
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#webpage = r"https://twitter.com/signup" # Twitter Signup apge
name = random.choice(open('Names.txt').readlines())
email = ""
password = ""


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

'''


driver = webdriver.Chrome()
driver.get(webpage)

sbox = driver.find_element_by_id("full-name")
sbox.send_keys(searchterm)

submit = driver.find_element_by_class_name("sbtSearch")
submit.click()


data = {
        "name" : name,
        "email" : email,
        "pass" : password
       }

encoded_data = urllib.urlencode(data)
content = urllib2.urlopen("http://www.abc.com/messages.php?action=send",
        encoded_data)
print content.readlines()
'''
