#! python3

import webbrowser, sys, pyperclip, requests, selenium, bs4, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Globals
initial_browser_url = "https://www.fieldglass.net/time_sheet_form.do"

def instantiate_Ie():
  #Set initial browser url
  webdriver.DesiredCapabilities.INTERNETEXPLORER["initialBrowserUrl"] = initial_browser_url
  #start the Ie browser
  browser = webdriver.Ie()
  return browser

#Globalize the instantiated Ie webdriver
driver = instantiate_Ie()
time.sleep(5)

def login_fg(): 
  #fg form values
  fieldglass_username = 'username'
  fieldglass_password = 'password'

  #username input
  elem = driver.find_element_by_name('username')
  elem.clear()
  elem.send_keys(fieldglass_username)
  #password input
  elem = driver.find_element_by_name('password')
  elem.clear()
  elem.send_keys(fieldglass_password)
  elem.submit()

login_fg()










