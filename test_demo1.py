import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class Baseclass:
    pass


class Test_Swaglabs(Baseclass):
    def test_invokeurl(self):
        self.driver.get("https://www.saucedemo.com/")
        # self.driver.get("http://www.google.com")
        assert self.driver.title == "Swag Labs"

    @pytest.mark.parametrize("username, password", [("standard_user", "secret_sauce"),
                                                    ("performance_glitch_user1", "secret_sauce")])
    def test_login(self, username, password):
        # self.driver.find_element_by_id("user-name").send_keys(username)
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        time.sleep(3)
        self.driver.find_element_by_id("password").send_keys(password)
        time.sleep(3)
        self.driver.find_element_by_id("login-button").click()
        time.sleep(3)

    def test_menu(self):
        self.driver.find_element_by_id("react-burger-menu-btn").click()




