from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage

class TestForgotPassword:
    def test_go_to_forgot_password(self, driver):
        main_page = MainPage(driver)
        main_page.open_page("/")
        main_page.click_personal_account()
        login_page = LoginPage(driver)
        login_page.click_forgot_password()
        login_page.wait_for_url("forgot-password")
        assert "forgot-password" in login_page.get_current_url()

    def test_input_email_and_restore(self, driver):
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.open_page("/forgot-password")
        forgot_page.enter_email_and_click_restore("test@yandex.ru")
        forgot_page.wait_for_url("reset-password")
        assert "reset-password" in forgot_page.get_current_url()

    def test_show_password_makes_field_active(self, driver):
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.open_page("/forgot-password")
        forgot_page.enter_email_and_click_restore("test@yandex.ru")
        forgot_page.click_show_password()
        assert forgot_page.is_password_field_active()