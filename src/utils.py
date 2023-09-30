from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import json
import jsonpath

def open_browser(url):
   global driver

   driver = webdriver.Chrome(executable_path="/Users/pavankumar/VSCODE/eastvantage-assign/chromedriver")    
   driver.maximize_window()
   driver.get(url)

   driver.find_element_by_xpath("//button[contains(text(),'Allow all cookies' )]").click()
   

def close_browser():
    driver.quit()


def get_element(location_name):
    """to access the element using the jsonpath provided"""
    file_path = open("/Users/pavankumar/VSCODE/eastvantage-assign/Locators/locators.json", "r", encoding="UTF-8")
    response = json.loads(file_path.read())
    value = jsonpath.jsonpath(response, location_name)
    file_path.close()
    return value[0]


def get_constant_data(location_name):
    """to access the constane value using the jsonpath provided"""
    file_path = open("/Users/pavankumar/VSCODE/eastvantage-assign/Locators/consant.json", "r", encoding="UTF-8")
    response = json.loads(file_path.read())
    value = jsonpath.jsonpath(response, location_name)
    file_path.close()
    return value[0]