import time

import pytest

from src.pageObjects.home_page import Home_page
from src.pageObjects.login_page import LoginPage
from src.utilities.logger import LogGen
from src.utilities.read_config import ReadConfig

@pytest.mark.usefixtures("setup")
class Test_002_Create_User:
    baseURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getEmail()


    verification_code = ReadConfig.get_verification_code()
    new_email = ReadConfig.get_new_email()
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_create_new_user(self):
        self.logger.info("Test_002_Create_User")
        self.logger.info("Starting_Test_create_new_user")
        #self.driver = setup
        # self.driver.get(self.baseURL)
        self.driver.get("https://amazon.in")
        self.driver.get("https://qat.aufgang.ai/auth")
        self.lp = LoginPage(self.driver)
        self.lp.click_login_with_verification_code()
        self.lp.set_email(self.email)
        self.lp.click_send_code()
        self.lp.set_verification_code(self.verification_code)
        self.lp.click_login()
        self.Hp = Home_page(self.driver)
        self.Hp.click_user_management()
        self.Hp.click_create_new_user()
        self.Hp.add_new_email(self.new_email)
        self.Hp.click_radio_user()
        self.Hp.click_create_user()








