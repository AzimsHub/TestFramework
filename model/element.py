class Element:

    def __init__(self,  by, value):
        self.by = by
        self.value = value

    def send_keys(self, text):
        """ Override send keys so we can log contents """
        log.info(f"Sending text {text} to {self}")
        self.element.send_keys(text)

