from selenium.webdriver.common.by import By
from model.element import Element
from model.page import Page


class HudlHomePage(Page):
    hudl_header = Element(By.CSS_SELECTOR, 'header[class="mainnav mainnav--hide-mobile mainnav--de elite-header "]')
    log_in_button = Element(By.CSS_SELECTOR, 'a[data-qa-id="login-select"]')

    _verify = [hudl_header, log_in_button]
