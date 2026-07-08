import allure
from pages.base_page import BasePage
from locators.locators import LoginPageLocators

class LoginPage(BasePage):
    @allure.step("Авторизация пользователя")
    def login(self, email, password):
        self.set_text_to_element(LoginPageLocators.EMAIL_INPUT, email)
        self.set_text_to_element(LoginPageLocators.PASSWORD_INPUT, password)
        self.wait_and_click(LoginPageLocators.LOGIN_BUTTON)
        self.wait_for_element_invisibility(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Переход на страницу восстановления пароля")
    def click_forgot_password(self):
        self.wait_and_click(LoginPageLocators.FORGOT_PASSWORD_LINK)