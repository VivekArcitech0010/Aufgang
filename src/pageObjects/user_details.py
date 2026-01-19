from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class UserDetails:
    #locators
    textbox_first_name = (By.XPATH,"//input[@name='user_name']")
    textbox_last_name = (By.XPATH,"//input[@name='user_last_name']")
    text_box_phone_number = (By.XPATH,"//input[@type='tel']")
    text_box_location = (By.XPATH,"//input[@name='user_location']")
    button_proceed = (By.CSS_SELECTOR,"button.bg-brand-blue")
    designation_xpath = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[3]/div[2]/div/div/form/div[1]/div[1]/div/div/div/div')
    desi_arcitech = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[3]/div[2]/div/div/form/div[1]/div[1]/div/div/div/div[2]/ul/li[1]')
    suggestion_first = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[3]/div[2]/div/div/form/div[1]/div[2]/div[2]/div[3]/div/button[1]')
    gen_ai = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[3]/div[2]/div/div/form/div[2]/div[2]/div/button/span[2]')
    proceed_xpath = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[4]/div/div[2]/button[2]')



    def __init__(self, driver):
        self.driver = driver

    def set_first_name(self, first_name):
        self.driver.find_element(*self.textbox_first_name).clear()
        self.driver.find_element(*self.textbox_first_name).send_keys(first_name)

    def set_last_name(self, last_name):
        self.driver.find_element(*self.textbox_last_name).clear()
        self.driver.find_element(*self.textbox_last_name).send_keys(last_name)

    def set_phone_number(self, phone_number):
        self.driver.find_element(*self.text_box_phone_number).clear()
        self.driver.find_element(*self.text_box_phone_number).send_keys(phone_number)

    def set_location(self, location):
        self.driver.find_element(*self.text_box_location).clear()
        self.driver.find_element(*self.text_box_location).send_keys(location)

    def click_proceed(self):
        self.driver.find_element(*self.button_proceed).click()

    def click_designation(self):
        self.driver.find_element(*self.designation_xpath).click()

    def click_arcitech(self):
        self.driver.find_element(*self.desi_arcitech).click()

    def click_suggestion_first(self):
        self.driver.find_element(*self.suggestion_first).click()

    def generate_ai(self):
        self.driver.find_element(*self.gen_ai).click()

    def click_process(self):
        self.driver.find_element(*self.proceed_xpath).click()

