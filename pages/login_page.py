from selenium.webdriver.common.by import By
from model.element import Element
from model.page import Page


class LogInPage(Page):
    user_name_field = Element(By.CSS_SELECTOR, 'input[data-qa-id="email-input"]')
    password_field = Element(By.CSS_SELECTOR, 'input[data-qa-id="password-input"]')
    log_in_button = Element(By.CSS_SELECTOR, 'button[data-qa-id="login-btn"]')
    error_message = Element(By.CSS_SELECTOR, 'p[data-qa-id="error-display"]')
