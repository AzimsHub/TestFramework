from selenium.webdriver.common.by import By
from model.element import Element
from model.page import Page


class OrgLoginPage(Page):
    log_in_field = Element(By.ID, 'uniId_1')
    org_log_in_button = Element(By.CSS_SELECTOR, 'button[data-qa-id="log-in-with-sso"]')

    _verify = [log_in_field]