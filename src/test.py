import utils as util
from utils import  get_constant_data, get_element
from robot.api import logger
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



def click_login():
    """clicks on login button"""
    util.driver.find_element_by_link_text(get_element("locators.eastvantage.login_btn")).click()

def enter_username():
    util.driver.find_element_by_css_selector(get_element("locators.eastvantage.usr_name")).send_keys(get_constant_data("data.valid_email"))

def enter_pwd():
    util.driver.find_element_by_css_selector(get_element("locators.eastvantage.password")).send_keys(get_constant_data("data.valid_pwd"))

def click_login_auth_screen():
    util.driver.find_element_by_css_selector(get_element("locators.eastvantage.login_auth_screen")).click()

def verify_login():
    home_btn = util.driver.find_element_by_partial_link_text("Home").is_displayed()

    assert home_btn == True

def click_submit_application():
    util.driver.find_element_by_css_selector(get_element("locators.eastvantage.submit_application")).click()

def click_submit_new_application():
    """scroll dowm and click on submit new application"""
    time.sleep(2)
    util.driver.execute_script("window.scrollTo(0, 1000)")
    util.driver.find_element_by_partial_link_text(get_element("locators.eastvantage.submit_application_new")).click()

def enter_first_name(frist_name):
    global first_name 
    first_name = frist_name
    util.driver.find_element_by_css_selector(get_element("locators.eastvantage.first_name")).send_keys(frist_name)

def enter_last_name():
    global last_name
    last_name = get_constant_data("data.last_name")
    util.driver.find_element_by_css_selector(get_element("locators.eastvantage.last_name")).send_keys(last_name)

def enter_address():
    global address
    address = get_constant_data("data.address")
    util.driver.find_element_by_css_selector(get_element("locators.eastvantage.address")).send_keys(address)

def enter_postcode():
    """enter postal code as 1000 and click enter"""
    global postal_code_enter
    postal_code = get_constant_data("data.postal_code")
    
    util.driver.find_element_by_css_selector(get_element("locators.eastvantage.postal_code")).send_keys(postal_code)
    time.sleep(3)
    
    action = ActionChains(util.driver)  
    # down key action
    action.send_keys(Keys.ARROW_DOWN).perform()
    action.send_keys(Keys.ENTER).perform()
    time.sleep(3)
    postal_code_enter = util.driver.find_element_by_css_selector(get_element("locators.eastvantage.postal_code")).text

def select_country_india():
    """select country as india by value "IN"""
    global country
    country = get_constant_data("data.country")
    select = Select(util.driver.find_element_by_id(get_element("locators.eastvantage.country")))
    select.select_by_value("IN")
    
def upload_image():
    """upload a image from local machine"""
    # click on uplaod button
    upload = util.driver.find_element_by_css_selector(get_element("locators.eastvantage.upload_button"))
    # upload a image from local machine
    image_path = '/Users/pavankumar/VSCODE/eastvantage-assign/file_example_PNG_500kB.png' 
    upload.send_keys(image_path)

def select_gender():
    """click on radio button male"""
    util.driver.find_element_by_css_selector(get_element("locators.eastvantage.select_male")).click()

def select_role():
    """select role """
    select = Select(util.driver.find_element_by_id(get_element("locators.eastvantage.role")))
    select.select_by_value("6365118b-637a-5297-b56d-e7c8b9a60ce0")
    global role
    role = util.driver.find_element_by_id(get_element("locators.eastvantage.role")).text

def select_tools():
    """click on robot framework readio button"""
    util.driver.find_element_by_css_selector(get_element("locators.eastvantage.robot_framwork")).click()

def enter_career_objective():
    """switch to frame 0 and enter carrer objective"""
    util.driver.switch_to.frame(0)
    util.driver.find_element_by_css_selector(get_element("locators.eastvantage.frame_body")).send_keys(get_constant_data("data.carreer_objective"))
    util.driver.switch_to.default_content()

def click_next():
    """click on next button"""
    util.driver.find_element_by_css_selector(get_element("locators.eastvantage.next_button")).click()


def verify_summary_details():
    """assert the summary details"""

    first_name_summary = util.driver.find_element_by_css_selector(get_element("locators.eastvantage.firstname_summary")).text
    last_name_summary = util.driver.find_element_by_css_selector(get_element("locators.eastvantage.lastname_summary")).text
    address_summary = util.driver.find_element_by_css_selector(get_element("locators.eastvantage.address_summary")).text
    postal_code_summary = util.driver.find_element_by_css_selector(get_element("locators.eastvantage.postal_summary")).text
    country_summary = util.driver.find_element_by_css_selector(get_element("locators.eastvantage.country_summary")).text
    tools_summary = util.driver.find_element_by_css_selector(get_element("locators.eastvantage.tools_summary")).text

    assert first_name_summary == first_name
    assert last_name_summary == last_name
    assert address_summary == address
    assert postal_code_summary == postal_code_enter
    assert country_summary == country
    assert tools_summary == "Robot Framework"
