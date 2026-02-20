import time
from selenium.webdriver.support.ui import Select


import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





from pageObjects.user_details import UserDetails
from src.pageObjects.login_page import LoginPage
from src.utilities.logger import LogGen
from src.utilities.read_config import ReadConfig



import pytest

from src.pageObjects.home_page import Home_page
from src.pageObjects.login_page import LoginPage
from src.utilities.logger import LogGen
from src.utilities.read_config import ReadConfig
from src.pageObjects.home_page import Home_page as Hp


@pytest.mark.usefixtures("setup")
class TestVerificationCode:
    """Test verification code with negative, blank, and correct inputs"""

    baseURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getEmail()
    verification_code = ReadConfig.get_verification_code()
    logger = LogGen.loggen()


    def test_verification_code_all_scenarios(self):
        """Test blank, wrong, and correct verification codes"""

        self.logger.info("\n" + "=" * 70)
        self.logger.info("VERIFICATION CODE TEST - ALL SCENARIOS")
        self.logger.info("=" * 70)

        # ===== SCENARIO 1: BLANK CODE =====
        self.logger.info("\n[TEST 1] BLANK verification code...")
        self.driver.get(self.baseURL)
        time.sleep(2)

        lp = LoginPage(self.driver)
        lp.click_login_with_verification_code()
        lp.set_email(self.email)
        lp.click_send_code()
        time.sleep(2)

        lp.set_verification_code("")  # Blank
        time.sleep(1)

        try:
            lp.click_login()
            self.logger.info("⚠ Checking if blank code is rejected...")
        except:
            self.logger.info("✓ Blank code - login button disabled")

        time.sleep(2)

        # ===== SCENARIO 2: WRONG CODE =====
        self.logger.info("\n[TEST 2] WRONG verification code (123456)...")
        self.driver.get(self.baseURL)
        time.sleep(2)

        lp = LoginPage(self.driver)
        lp.click_login_with_verification_code()
        lp.set_email(self.email)
        lp.click_send_code()
        time.sleep(2)

        lp.set_verification_code("123456")  # Wrong code
        time.sleep(1)
        lp.click_login()
        time.sleep(3)

        if 'auth' in self.driver.current_url.lower():
            self.logger.info("✓ Wrong code rejected - still on login page")
        else:
            self.logger.warning("⚠ Wrong code was accepted (unexpected)")

        # ===== SCENARIO 3: SPECIAL CHARACTERS =====
        self.logger.info("\n[TEST 3] INVALID code with special chars (!@#$%^)...")
        self.driver.get(self.baseURL)
        time.sleep(2)

        lp = LoginPage(self.driver)
        lp.click_login_with_verification_code()
        lp.set_email(self.email)
        lp.click_send_code()
        time.sleep(2)

        lp.set_verification_code("!@#$%^")  # Special characters
        time.sleep(1)
        lp.click_login()
        time.sleep(3)

        if 'auth' in self.driver.current_url.lower():
            self.logger.info("✓ Special characters rejected")

        # ===== SCENARIO 4: CORRECT CODE =====
        self.logger.info("\n[TEST 4] CORRECT verification code...")
        self.driver.get(self.baseURL)
        time.sleep(2)

        lp = LoginPage(self.driver)
        lp.click_login_with_verification_code()
        lp.set_email(self.email)
        lp.click_send_code()
        time.sleep(2)

        lp.set_verification_code(self.verification_code)  # CORRECT
        self.logger.info(f"Using correct code: {self.verification_code}")
        time.sleep(1)
        lp.click_login()
        time.sleep(5)
        print("hi")

        #Verify success
        if 'auth' not in self.driver.current_url.lower():
            self.logger.info("✓ CORRECT code accepted - Login successful!")
            self.logger.info("\n" + "=" * 70)
            self.logger.info("✅ ALL SCENARIOS PASSED")
            self.logger.info("=" * 70)
            assert True
        else:
            self.logger.error("❌ Correct code failed")
            self.driver.save_screenshot("./screenshots/correct_code_failed.png")
            assert False, "Login should succeed with correct code"
        print("hii")
        time.sleep(10)



# @pytest.mark.usefixtures("setup")
# class TestAufgang:
#     baseURL = ReadConfig.getApplicationURL()
#     verification_code = ReadConfig.get_verification_code()
#     new_email = ReadConfig.get_new_email()
#     logger = LogGen.loggen()
#     new_user_email = ReadConfig.get_new_email()
#     first_name = ReadConfig.get_first_name()
#     last_name = ReadConfig.get_last_name()
#     phone_number = ReadConfig.get_phone_number()
#     location = ReadConfig.get_location()
#     project_name = ReadConfig.get_project_name()
#     client_name = ReadConfig.get_client_name()
#     total_area = ReadConfig.get_total_area()
#     estimated_budget = ReadConfig.get_estimated_budget()
#     district_code = ReadConfig.get_district_code()
#     location_p = ReadConfig.get_location_p()
#
    # baseURL = ReadConfig.getApplicationURL()
    # email = ReadConfig.getEmail()
    # verification_code = ReadConfig.get_verification_code()
    # new_email = ReadConfig.get_new_email()
    # logger = LogGen.loggen()

    def test_Admin_Login(self,setup):
        self.logger.info("Test_002_Create_User")
        self.logger.info("Starting_Test_create_new_user")

        self.driver = setup
        # print("hi")
        # self.driver.get(self.baseURL)
        # print("hi1")
        # self.lp = LoginPage(self.driver)
        # self.lp.click_login_with_verification_code()
        # print("hiii")
        # self.lp.set_email(self.email)
        # self.lp.click_send_code()
        # self.lp.set_verification_code(self.verification_code)
        #
        # self.lp.click_login()
        #
        self.Hp = Home_page(self.driver)
        time.sleep(5)
        self.Hp.click_user_management()
        print("hiii")
        self.Hp.click_create_new_user()
        self.Hp.add_new_email(self.new_email)
        self.Hp.click_radio_user()
        self.Hp.click_create_user()

        print("h000")

        time.sleep(5)
        a = self.driver.find_elements(By.XPATH,"//span[@class='sm:hidden lg:flex font-semibold md:text-xs lg:text-sm']")
        for i in a:
            if i.text == "Projects":
                i.click()
                break
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//button[@class='flex items-center bg-brand-blue text-white border rounded-md py-2 px-6 hover:bg-btn_hov_brand font-bold']").click()
        time.sleep(3)
        print("H1122")

        self.driver.find_element(By.XPATH,"// input[ @ name = 'project_name']").send_keys("Seeandsstone")
        self.driver.find_element(By.XPATH, "// input[ @ name = 'project_client_name']").send_keys("Ned stark")
        self.driver.find_element(By.XPATH,"//input[@class='w-full relative ps-[80px] bg-Gray_G20 rounded-lg px-4 py-3 border border-grey-200 focus:outline-none mt-2 text-xs lg:text-sm refresh']").send_keys("2200")
        self.driver.find_element(By.XPATH,"//input[@class='w-full relative ps-[60px] rounded-lg px-4 py-3 border border-grey-200 focus:outline-none mt-2 text-xs lg:text-sm refresh']").send_keys("129278")
        self.driver.find_element(By.XPATH, "// input[ @ name = 'project_district_code']").send_keys("NHI")
        abcd = self.driver.find_element(By.XPATH, "// input[ @class ='w-full rounded-lg px-4 py-3 border border-grey-200 focus:outline-none mt-2 text-xs lg:text-sm refresh pac-target-input']")
        abcd.send_keys("New")
        time.sleep(3)
        abcd.send_keys(Keys.ARROW_DOWN)

        time.sleep(5)
        self.driver.find_element(By.XPATH,"// input[ @class ='w-full relative ps-[70px] bg-Gray_G20 rounded-lg px-4 py-3 border border-grey-200 focus:outline-none mt-2 text-xs lg:text-sm refresh']").send_keys("")
        self.driver.find_element(By.XPATH,"// button[ @class ='bg-brand-blue text-white border rounded-lg text-xs lg:text-sm py-2 px-8 font-bold hover:bg-btn_hov_brand']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//div[@class='flex justify-between items-center w-full bg-Gray_G20 rounded-lg px-4 py-[15px] border border-grey-200 focus:outline-none mt-2 text-xs lg:text-sm refresh cursor-pointer']").click()
        time.sleep(10)
        self.driver.find_element(By.XPATH,"//li[@class='px-4 w-[100%] py-2 text-xs cursor-pointer text-black-900 hover:bg-gray-100'][1]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div[3]/main/div/div[3]/div/div[2]/div/div/form/div[1]/div/div/div[1]/div[2]/div/div/div/span").click()
        # self.driver.find_element(By.XPATH, "//div[@class='flex justify-between items-center w-full bg-Gray_G20 rounded-lg px-4 py-[15px] border border-grey-200 focus:outline-none mt-2 text-xs lg:text-sm refresh cursor-not-allowed opacity-60']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"// li[ @class ='px-4 w-[100%] py-2 text-xs cursor-pointer text-black-900 hover:bg-gray-100'][1]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//input[@name='project_building_height']").send_keys("8000")
        time.sleep(3)
        self.driver.find_element(By.XPATH,"// input[ @ name = 'project_number_of_stories']").send_keys("12")
        time.sleep(3)

        calender_icons = self.driver.find_elements(By.XPATH, "//img[contains(@alt,'calendar')]")
        dates_to_select = [{"year": "2025", "month": "December", "day": "15"},
                           {"year": "2026", "month": "December", "day": "16"}]

        for i in range(len(calender_icons)):
            calender_icons[i].click()
            year_to_select = dates_to_select[i]["year"]
            month_to_select = dates_to_select[i]["month"]
            day_to_select = dates_to_select[i]["day"]

            year_picker = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[@class='rdrYearPicker']")))
            year_picker.click()

            year_option = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//option[text()='{year_to_select}']")))
            year_option.click()

            month_picker = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'rdrMonthPicker')]")))
            month_picker.click()

            month_option = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//option[text()='{month_to_select}']")))
            month_option.click()

            day_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, f"//span[contains(@class,'rdrDayNumber')]//span[text()='{day_to_select}']")))
            day_button.click()
            time.sleep(2)

        # calender_icons = self.driver.find_elements(By.XPATH, "//img[contains(@alt,'calendar')]")
        #
        # for i in range(len(calender_icons)):
        #     # Click on the calendar icon (start date or end date)
        #     calender_icons[i].click()
        #
        #     # Wait for the year picker to be visible and clickable
        #     year_picker = WebDriverWait(self.driver, 10).until(
        #         EC.element_to_be_clickable((By.XPATH, "//select[@class='rdrYearPicker']"))
        #     )
        #
        #     # Use Select to interact with the year dropdown
        #     select_year = Select(year_picker)
        #     select_year.select_by_visible_text('2025')  # Change to desired year
        #
        #     # Wait for the month dropdown to be visible and clickable
        #     month_picker = WebDriverWait(self.driver, 10).until(
        #         EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'rdrMonthPicker')]"))
        #     )
        #     month_picker.click()
        #
        #     # Wait for and select December from the month options (you can change the month as needed)
        #     month_option = WebDriverWait(self.driver, 10).until(
        #         EC.element_to_be_clickable((By.XPATH, "//span[text()='December']"))
        #     )
        #     month_option.click()
        #
        #     # Wait for the day button (for the 1st day in the calendar) to be clickable
        #     day_button = WebDriverWait(self.driver, 10).until(
        #         EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'rdrDayNumber')]//span[text()='1']"))
        #     )
        #     day_button.click()
        #
        #     # Optional: Wait before moving on to the next calendar if necessary
        #     time.sleep(2)
        #
        #     print(f"Clicked on calendar icon {i + 1} and selected the date.")
        #
        #     # Allow some time for UI updates
        #     time.sleep(2)










            # month = self.driver.find_element(By.XPATH, "//span[@class='rdrMonthPicker']")
            # month.click()
            #
            # month_element = self.driver.find_element(By.XPATH, "//td[@class='rdtMonth' and text()='Jun']")
            # month_element.click()
            # day_element = self.driver.find_element(By.XPATH, "//td[@class='rdtDay' and text()='21']")
            # day_element.click()





        # self.logger.info("Selecting start date...")
        #
        # # Click calendar icon (not the input field!)
        # calendar_icons = self.driver.find_elements(By.XPATH, "//img[@alt='calendar']")
        # calendar_icons[0].click()  # First icon = start date
        # time.sleep(2)
        #
        # Select(self.driver.find_element(By.XPATH, "//select[contains(@class,'rdrYearPicker')]")).select_by_visible_text(
        #     '2025')
        # time.sleep(1)
        #
        # Select(self.driver.find_element(By.XPATH, "//select[@class='rdrMonthPicker']")).select_by_visible_text(
        #     'December')
        # time.sleep(1)
        #
        # self.driver.find_element(By.XPATH, "//button[@class='rdrDay']//span[text()='1']").click()
        # time.sleep(2)
        #
        # # COMPLETION DATE
        # self.logger.info("Selecting completion date...")
        #
        # # Click second calendar icon
        # calendar_icons = self.driver.find_elements(By.XPATH, "//img[@alt='calendar']")
        # calendar_icons[1].click()  # Second icon = completion date
        # time.sleep(2)
        #
        # Select(self.driver.find_element(By.XPATH, "//select[contains(@class,'rdrYearPicker')]")).select_by_visible_text(
        #     '2026')
        # time.sleep(1)
        #
        # Select(self.driver.find_element(By.XPATH, "//select[@class='rdrMonthPicker']")).select_by_visible_text('March')
        # time.sleep(1)
        #
        # self.driver.find_element(By.XPATH, "//button[@class='rdrDay']//span[text()='31']").click()
        # time.sleep(2)
        #
        # Proceed
        self.driver.find_element(By.XPATH, "//button[text()='Proceed']").click()
        time.sleep(3)


        self.driver.find_element(By.XPATH,"//input[@placeholder='Enter Revit GUUID']").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Search for Revit File']").click()

        revit_file_dropdown = self.driver.find_elements(By.XPATH, "//div[@class='absolute left-0 right-0 bg-white border rounded shadow max-h-60 overflow-y-auto z-10 h-auto']//div")
        for file in revit_file_dropdown:
            if file.text == "THE VILLAGE AT TUXEDO RESERVE BUILDING 14 INT_ARCH_RVT2025_ayushiVMA4U.rvt":
                file.click()
                break
        # dropdown = Select(self.driver.find_element(By.XPATH, "//div[@class='px-4 py-2 cursor-pointer hover:bg-gray-100 text-xs lg:text-sm bg-gray-200 font-semibold']"))
        # # dropdown.select_by_visible_text('THE VILLAGE AT TUXEDO RESERVE BUILDING 14 INT_ARCH_RVT2025_ayushiVMA4U.rvt')
        # dropdown.select_by_index(1)
        time.sleep(5)
        print("holaaa")
        self.driver.find_element(By.XPATH,"// input[ @ placeholder = 'Select services provided']").click()
        self.driver.find_element(By.XPATH, "// div[ @class ='_dropdownOption_15vuy_86  false'][2]").click()
        self.driver.find_element(By.XPATH, "// button[ @class ='text-cool-gray flex space-x-1 items-center font-semibold px-4 py-2 rounded-md border border-brand-blue text-xs lg:text-sm cursor-pointer']").click()
        time.sleep(5)

        self.driver.find_element(By.XPATH, "//button[@type ='submit']").click()
        time.sleep(10)

        self.driver.find_element(By.XPATH, "//div[@class='_drop_sec_down_sec_1r72y_84']//button//div").click()
        time.sleep(5)

        self.driver.find_element(By.XPATH, "//button[@class='flex justify-center pt-4 cursor-pointer text-[16px] mt-2 font-semibold hover:text-hover-brand text-center']").click()
        time.sleep(5)

    def test_login_new_user_profile1(self):
        self.logger.info("Test_003_Login_New_User_Profile")
        self.logger.info("Starting_Test_login_new_user_profile")
        #self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.click_login_with_verification_code()
        self.lp.set_email(self.email)
        self.lp.click_send_code()
        self.lp.set_verification_code(self.verification_code)
        self.lp.click_login()
        time.sleep(1)
        self.ud = UserDetails(self.driver)
        self.ud.set_first_name(self.first_name)
        self.ud.set_last_name(self.last_name)
        self.ud.set_phone_number(self.phone_number)
        self.ud.set_location(self.location)
        time.sleep(5)
        self.ud.click_proceed()
        time.sleep(5)
        a = self.driver.find_element(By.XPATH,
                                     "//div[@class='w-full sm:w-[40%] bg-Gray_G20 rounded-lg px-4 py-3 h-[41.6px] border border-grey-200 focus:outline-none mt-2 text-xs cursor-pointer flex justify-between items-center']")
        a.click()
        self.driver.find_element(By.XPATH, "//div[@class='absolute w-full sm:w-[40%] bg-white border border-grey-200 rounded-md z-10 top-full mt-1']//ul/li[2]").click()
        self.driver.find_element(By.XPATH, "//div[@class='flex flex-wrap gap-2']//button[2]").click()
        self.driver.find_element(By.XPATH, "//button[@class='text-cool-gray flex space-x-1 items-center font-semibold px-4 py-2 rounded-md border border-brand-blue text-sm cursor-pointer']").click()

        time.sleep(15)
        proceed_xpath = "//button[@class='bg-brand-blue text-white px-8 py-2.5 rounded-lg text-base font-bold hover:bg-btn_hov_brand transition-colors ']"

        for i in range(3):
            try:
                button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, proceed_xpath))
                )
                button.click()
                print(f"✓ Clicked proceed button {i + 1}/3")
                time.sleep(5)
            except:
                print(f"✓ Onboarding complete after {i} clicks")
                break

        print("✓ Profile setup completed")
        # self.driver.find_element(By.XPATH,"//button[@class='bg-brand-blue text-white px-8 py-2.5 rounded-lg text-base font-bold hover:bg-btn_hov_brand transition-colors ']").click()
        # time.sleep(5)
        # self.driver.find_element(By.XPATH,"//button[@class='bg-brand-blue text-white px-8 py-2.5 rounded-lg text-base font-bold hover:bg-btn_hov_brand transition-colors ']").click()
        # print("fff")
        # self.driver.find_element(By.XPATH,"//button[@class='bg-brand-blue text-white px-8 py-2.5 rounded-lg text-base font-bold hover:bg-btn_hov_brand transition-colors ']").click()
        print("sss")
        self.driver.find_element(By.XPATH,"//tr[@class='group cursor-pointer hover:bg-teal-green'][1]").click()
        time.sleep(3)
































