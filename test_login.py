from selenium import webdriver
from pages.login_page import LogInPage
from pages.home_page import HomePage
from pages.hudl_home import HudlHomePage
import time
import pytest
import os


@pytest.fixture
def driver_url_fixture():
    return "https://www.hudl.com/login"


@pytest.fixture
def driver_fixture(driver_url_fixture):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(driver_url_fixture)
    yield driver
    driver.close()
    driver.quit()


def test_successful_log_in(driver_fixture):
    browser = driver_fixture

    login_page = LogInPage(browser)

    login_page.user_name_field.send_keys(os.environ.get('HUDL_USERNAME'))
    login_page.password_field.send_keys(os.environ.get('HUDL_PASSWORD'))
    login_page.log_in_button.click()

    assert HomePage(browser)


def test_unsuccessful_log_in(driver_fixture):
    browser = driver_fixture

    login_page = LogInPage(browser)

    login_page = LogInPage(browser)
    login_page.user_name_field.send_keys("ab")
    login_page.password_field.send_keys("ab")
    login_page.log_in_button.click()

    assert login_page.error_message.is_displayed


def test_successful_log_out(driver_fixture):
    browser = driver_fixture

    login_page = LogInPage(browser)

    login_page.user_name_field.send_keys(os.environ.get('HUDL_USERNAME'))
    login_page.password_field.send_keys(os.environ.get('HUDL_PASSWORD'))
    login_page.log_in_button.click()

    home_page = HomePage(browser)
    home_page.account_button.click()
    home_page.log_out_button.click()

    assert HudlHomePage(browser)
