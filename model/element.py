class Element:

    def __init__(self,  by, value):
        self.by = by
        self.value = value
        self.driver = None

    def send_keys(self, text):
        """ Override send keys so we can log contents """
        self.find_element().send_keys(text)

    def find_element(self):
        return self.driver.find_element(self.by, self.value)

    def click(self):
        self.find_element().click()

    def scroll_to(self, arg1, arg2):
        self.find_element().scroll_to(arg1, arg2)

    def is_displayed(self):
        self.find_element().is_displayed()


