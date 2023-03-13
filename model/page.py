from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from model.element import Element


class Page:

    _verify = None

    def __init__(self, driver):
        self.driver = driver

        # Loop through attributes of this instance, save any Element objects to a list
        my_elements = []
        for x in dir(self):
            my_element = getattr(self, x)
            if isinstance(my_element, Element):
                my_elements.append(my_element)

        # For each of the Element objects, set the driver attributes so the element can access the browser
        for element in my_elements:
            element.driver = self.driver

        # wait until verify_on_load is successful
        self.verify_on_load()

    def verify_on_load(self):
        if self._verify:
            for element in self._verify:
                wait = WebDriverWait(self.driver, timeout=10, poll_frequency=1, ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
                wait.until(EC.element_to_be_clickable((element.by, element.value)))
