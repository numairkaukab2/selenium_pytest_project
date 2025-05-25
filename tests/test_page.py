from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pytest


test_data = [

    ("standard_user","secret_sauce", True), # Valid
    ("locked_out_user","secret_sauce", False), # Locked Out
    ("problem_user","secret_sauce", True), # Valid
    ("performance_glitch_user","secret_sauce", True), # Valid
    ("error_user","secret_sauce", True), # Valid
    ("visual_user","secret_sauce", True), # Valid
    ("", "", False),  # Both empty
    ("standard_user", "", False),  # Password missing
    ("", "secret_sauce", False),  # Username missing
    ("not_a_user", "wrong_pass", False),  # Wrong credentials
    ("   ", "   ", False),  # Spaces only
    ("<script>alert(1)</script>", "password", False),  # XSS
    ("' OR '1'='1", "anything", False),  # SQL injection
    ("user"*100, "pass"*100, False),  # Extremely long input
    ("standard_user", "wrong_pass", False),  # Correct user, wrong pass
    ("!@#$%^&*()", "password", False),  # Special chars


]

@pytest.mark.parametrize("user,pwd,should_succeed",test_data)
def test_page(driver, user, pwd, should_succeed):
    
    driver.get("http://www.saucedemo.com")
    login_page = LoginPage(driver)
    login_page.login(user,pwd)
    
    if should_succeed:

        assert driver.find_elements(By.CLASS_NAME, "app_logo"), "Expected Success"
    else:
        assert not driver.find_elements(By.CLASS_NAME, "app_logo"), "Expected Failure"
    