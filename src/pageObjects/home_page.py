from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Home_page:

    # Correct locator for User Management
    # button_user_management = (By.XPATH,"(//span[text()='User Management'])[2]")
    button_user_management = (By.XPATH, "//img[contains(@src,'231C1B')]")


    button_create_new_user = (By.CSS_SELECTOR,"span.mr-2")
    text_box_new_email = (By.CSS_SELECTOR,"input.bg-Gray_G20")
    radio_user = (By.XPATH,"//label[text()='User']")
    button = (By.XPATH,"//button[@type='submit']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def click_user_management(self):
        # wait for Toastify popup to go away
        # WebDriverWait(self.driver, 10).until(
        #     EC.invisibility_of_element_located((By.CSS_SELECTOR, ".Toastify__toast"))
        # )
        self.driver.find_element(*self.button_user_management).click()
        # element = WebDriverWait(self.driver, 20).until(
        #     EC.presence_of_element_located(self.button_user_management)
        # )

        # self.driver.execute_script("arguments[0].click();", element)
        #
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        # self.driver.execute_script("arguments[0].click();", element)

    def click_create_new_user(self):
        # WebDriverWait(self.driver, 10).until(
        #     EC.invisibility_of_element_located((By.CSS_SELECTOR, ".Toastify__toast"))
        # )
        self.driver.find_element(*self.button_create_new_user).click()

    def add_new_email(self,new_email):
        self.driver.find_element(*self.text_box_new_email).send_keys(new_email)

    def click_radio_user(self):
        self.driver.find_element(*self.radio_user).click()

    def click_create_user(self):
        self.driver.find_element(*self.button).click()
