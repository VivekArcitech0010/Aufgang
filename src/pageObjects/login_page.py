# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class LoginPage:
#     # Locators :
#     link_login_with_verification_code = (By.CSS_SELECTOR, "button.text-brand-blue")
#     textbox_email = (By.XPATH, "//input[@type='email']")
#     button_send_code = (By.XPATH, "//button[@type='submit']")
#     textbox_verification_code = (By.XPATH,"//input[@inputmode='numeric'][1]")
#     button_login = (By.CSS_SELECTOR,"button.bg-brand-blue")
#
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(self.driver, 10)
#
#     def click_login_with_verification_code(self):
#         element = self.wait.until(
#             EC.element_to_be_clickable(self.link_login_with_verification_code)
#         )
#         element.click()
#
#     def set_email(self,email):
#         self.driver.find_element(*self.textbox_email).clear()
#         self.driver.find_element(*self.textbox_email).send_keys(email)
#
#     def click_send_code(self):
#         self.driver.find_element(*self.button_send_code).click()
#
#     def set_verification_code(self,verification_code):
#         self.driver.find_element(*self.textbox_verification_code).clear()
#         self.driver.find_element(*self.textbox_verification_code).send_keys(verification_code)
#
#     def click_login(self):
#         self.driver.find_element(*self.button_login).click()
#         time.sleep(3)


import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException


class LoginPage:
    # Locators :
    link_login_with_verification_code = (By.CSS_SELECTOR, "button.text-brand-blue")
    textbox_email = (By.XPATH, "//input[@type='email']")
    button_send_code = (By.XPATH, "//button[@type='submit']")
    textbox_verification_code = (By.XPATH, "//input[@inputmode='numeric'][1]")
    button_login = (By.CSS_SELECTOR, "button.bg-brand-blue")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)  # Increased timeout to 20 seconds

    def click_login_with_verification_code(self):
        try:
            # Wait for page to be fully loaded
            self.wait.until(
                lambda driver: driver.execute_script("return document.readyState") == "complete"
            )

            # Wait for element to be visible first
            element = self.wait.until(
                EC.visibility_of_element_located(self.link_login_with_verification_code)
            )

            # Then wait for it to be clickable
            element = self.wait.until(
                EC.element_to_be_clickable(self.link_login_with_verification_code)
            )

            # Scroll element into view
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            time.sleep(0.5)  # Brief pause after scrolling

            element.click()

        except (TimeoutException, ElementClickInterceptedException) as e:
            # Fallback: Use JavaScript click
            print(f"Standard click failed, trying JavaScript click. Error: {e}")
            element = self.driver.find_element(*self.link_login_with_verification_code)
            self.driver.execute_script("arguments[0].click();", element)

    def set_email(self, email):
        element = self.wait.until(
            EC.visibility_of_element_located(self.textbox_email)
        )
        element.clear()
        element.send_keys(email)

    def click_send_code(self):
        element = self.wait.until(
            EC.element_to_be_clickable(self.button_send_code)
        )
        element.click()

    def set_verification_code(self, verification_code):
        element = self.wait.until(
            EC.visibility_of_element_located(self.textbox_verification_code)
        )
        element.clear()
        element.send_keys(verification_code)

    def click_login(self):
        element = self.wait.until(
            EC.element_to_be_clickable(self.button_login)
        )
        element.click()
        time.sleep(3)

