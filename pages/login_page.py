from selenium.webdriver.common.by import By
from model.element import Element
from model.page import Page


class LogInPage(Page):
    user_name_field = Element(By.CSS_SELECTOR, 'input[data-qa-id="email-input"]')
    password_field = Element(By.CSS_SELECTOR, 'input[data-qa-id="password-input"]')
    log_in_button = Element(By.CSS_SELECTOR, 'button[data-qa-id="login-btn"]')
    error_message = Element(By.CSS_SELECTOR, 'p[data-qa-id="error-display"]')
    remember_me_check_box = Element(By.CSS_SELECTOR, 'rect[class="uni-form__check-indicator__background"]')
    log_in_organisation = Element(By.CSS_SELECTOR, 'button[data-qa-id="log-in-with-organization-btn"]')

    _verify = [user_name_field, user_name_field, log_in_button]
