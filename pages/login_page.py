from pages.base_page import BasePage
from locators.locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    def login(self, email, password):
        self.set_text_to_element(LoginPageLocators.EMAIL_INPUT, email)
        self.set_text_to_element(LoginPageLocators.PASSWORD_INPUT, password)
        self.wait_and_click(LoginPageLocators.LOGIN_BUTTON)
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(LoginPageLocators.LOGIN_BUTTON))

    def click_forgot_password(self):
        self.wait_and_click(LoginPageLocators.FORGOT_PASSWORD_LINK)