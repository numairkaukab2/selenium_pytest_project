from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pytest


test_data = [

    ("standard_user","secret_sauce"),
    ("locked_out_user","secret_sauce"),
    ("problem_user","secret_sauce"),
    ("performance_glitch_user","secret_sauce"),
    ("error_user","secret_sauce"),
    ("visual_user","secret_sauce")


]

@pytest.mark.parametrize("user,pwd",test_data)
def test_page(driver, user, pwd):
    
    driver.get("http://www.saucedemo.com")
    login_page = LoginPage(driver)
    login_page.login(user,pwd)
    
    
    assert driver.find_elements(By.CLASS_NAME, "app_logo"), "Login Failed!"
    