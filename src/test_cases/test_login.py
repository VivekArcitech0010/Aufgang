import time

import pytest
from selenium.webdriver.common.by import By

from src.pageObjects.login_page import LoginPage
from src.utilities.read_config import ReadConfig
from src.utilities.logger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getEmail()


    verification_code = ReadConfig.get_verification_code()
    logger = LogGen.loggen()


    @pytest.mark.smoke
    def test_verify_page_title(self,setup):
        self.logger.info("Test_001_Login.test_verify_page_title")
        self.logger.info("Starting test_verify_page_title")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Aufgang":
            assert True
            self.driver.close()
            print("Actual_Title = ",act_title)
            self.logger.info("test_verify_page_title_PASSED")

        else :
            self.driver.save_screenshot(".\\Screenshots\\" + "test_verify_page_title.png")
            self.logger.info("test_verify_page_title_FAILED")
            assert False

    @pytest.mark.smoke
    def test_login(self,setup):
        self.logger.info("Test_001_Login.test_login")
        self.logger.info("Starting test_login")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.click_login_with_verification_code()
        self.lp.set_email(self.email)
        self.lp.click_send_code()
        self.lp.set_verification_code(self.verification_code)
        self.lp.click_login()
        try:
            text = self.driver.find_element(By.XPATH, "//span[text()='Project Name']").text
            if text == "Project Name":
                print("Test Passed")
                self.logger.info("Test_login_PASSED")
                assert True
            else:
                print("Test Failed")
                self.logger.error("Test_Login_FAILED")
                assert False

        except:
            print("Test Failed")
            self.logger.error("Test_Login_FAILED")
            self.driver.save_screenshot(".\\Screenshots\\test_login.png")
            assert False