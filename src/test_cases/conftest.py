import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield
    driver.quit()

# @pytest.fixture(scope="class")
# def Baseclass(request):
#     chrome_options = Options()
#     chrome_options.add_argument("--start-maximized")
#     service = ChromeService(executable_path="D:/Automation/drivers/chromedriver.exe")
#     driver = webdriver.Chrome(service=service, options=chrome_options)
#     request.cls.driver = driver
#     driver.get("https://qat.braen.ai")
#     driver.implicitly_wait(10)
#     time.sleep(2)
#     yield
#     driver.quit()