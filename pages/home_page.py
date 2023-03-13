from selenium.webdriver.common.by import By
from model.element import Element
from model.page import Page


class HomePage(Page):
    home_button = Element(By.CSS_SELECTOR, 'a[data-qa-id="webnav-globalnav-home"]')
    account_button = Element(By.CSS_SELECTOR, 'div[class="hui-globaluseritem"]')
    log_out_button = Element(By.LINK_TEXT, "Log Out")

    _verify = [home_button, account_button]
