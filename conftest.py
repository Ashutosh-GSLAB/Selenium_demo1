import pytest
from selenium import webdriver

@pytest.fixture(scope="class")                    # it will execute only once
def setup(request):                                # it executed first before testcase executing
    driver = webdriver.Chrome(executable_path="C:\\all_browser_exe_file\\chromedriver.exe")
    # driver.get("https://www.saucedemo.com/")
    request.cls.driver=driver                              # return driver object
    # yield
    # driver.close()



