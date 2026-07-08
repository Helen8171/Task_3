import allure
from pages.base_page import BasePage
from locators.locators import ForgotPasswordLocators

class ForgotPasswordPage(BasePage):
    @allure.step("Ввод email и клик по кнопке восстановления")
    def enter_email_and_click_restore(self, email):
        self.set_text_to_element(ForgotPasswordLocators.EMAIL_INPUT, email)
        self.wait_and_click(ForgotPasswordLocators.RESTORE_BUTTON)

    @allure.step("Клик по иконке показа пароля")
    def click_show_password(self):
        self.wait_and_click(ForgotPasswordLocators.SHOW_PASSWORD_ICON)

    @allure.step("Проверка активности поля пароля")
    def is_password_field_active(self):
        return self.check_element_is_visible(ForgotPasswordLocators.ACTIVE_PASSWORD_FIELD)