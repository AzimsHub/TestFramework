from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LogInPage
from pages.home_page import HomePage


# def test_login():
#     driver = webdriver.Chrome()
#     driver.get("https://www.hudl.com/login")
#
#     log_in_field = driver.find_element(By.CSS_SELECTOR, 'input[data-qa-id="email-input"]')
#     password_field = driver.find_element(By.CSS_SELECTOR, 'input[data-qa-id="password-input"]')
#     log_in_button = driver.find_element(By.CSS_SELECTOR, 'button[data-qa-id="login-btn"]')
#
#     log_in_field.send_keys("azim.chowdhury@hotmail.com")
#     password_field.send_keys("Pass123$")
#     log_in_button.click()
#
#     assert driver.find_element(By.CSS_SELECTOR, 'a[data-qa-id="webnav-globalnav-home"]')


def test_successful_log_in():
    # TODO page take browser as arg
    # TODO access browser in Element, wait etc.
    # TODO override selenium element functions in Element

    login_page = LogInPage(browser)
    login_page.user_name_field.send_keys("environ.login")
    login_page.password_field.send_keys("environ.password")
    login_page.log_in_button.click()

    assert HomePage()


def test_unsuccessful_log_in():

    login_page = LogInPage(browser)
    login_page.user_name_field.send_keys("ab")
    login_page.password_field.send_keys("ab")
    login_page.log_in_button.click()

    assert error_message.isDisplayed







