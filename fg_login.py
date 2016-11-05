#! python3

import webbrowser, sys, pyperclip, requests, selenium, bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


initial_browser_url = "https://www.fieldglass.net/time_sheet_form.do"

def instantiate_Ie():
  webdriver.DesiredCapabilities.INTERNETEXPLORER["initialBrowserUrl"] = initial_browser_url
  browser = webdriver.Ie()
  return browser

driver = instantiate_Ie()
fieldglass_username = "field glass username goes here"
fieldglass_password = "fieldglass password goes here"
driver.implicitly_wait(3)
elem = driver.find_element_by_name('username')
elem.clear()
elem.send_keys(fieldglass_username)
elem = driver.find_element_by_name('password')
elem.send_keys(fieldglass_password)
elem.submit()











