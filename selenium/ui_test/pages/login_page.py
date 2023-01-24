import time
from libraries import mapping, mouse, forms


class Login:

    def __init__(self, driver):
        self.driver = driver
        self.log_in_button = "//*[@id='login2']"
        self.user_txt = "//*[@id='loginusername']"
        self.user_password_txt = "//*[@id='loginpassword']"
        self.sign_in_button = "//*[@id='logInModal']/div/div/div[3]/button[2]"

    def load(self):
        url = mapping.map_environment()
        self.driver.get(url)

    def click_on_log_in_button(self):
        mouse.click_on_element(self, "XPATH", self.log_in_button)

    def type_user_name(self, name):
        time.sleep(2)
        forms.enter_text_on_element(self, "XPATH", self.user_txt, name)

    def type_password(self, password):
        forms.enter_text_on_element(self, "XPATH", self.user_password_txt, password)

    def click_on_sign_in_button(self):
        mouse.click_on_element(self, "XPATH", self.sign_in_button)

