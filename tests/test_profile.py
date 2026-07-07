from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


class TestProfile:
    def test_go_to_profile_page(self, driver, created_user):
        user_data, _ = created_user
        main_page = MainPage(driver)
        main_page.open_page("/")
        main_page.click_personal_account()

        login_page = LoginPage(driver)
        login_page.login(user_data["email"], user_data["password"])
        main_page.click_personal_account()
        main_page.wait_for_url("account")
        assert "account" in driver.current_url

    def test_go_to_order_history(self, driver, created_user):
        user_data, _ = created_user
        main_page = MainPage(driver)
        main_page.open_page("/")
        main_page.click_personal_account()

        login_page = LoginPage(driver)
        login_page.login(user_data["email"], user_data["password"])
        main_page.click_personal_account()

        profile_page = ProfilePage(driver)
        profile_page.click_order_history()
        profile_page.wait_for_url("order-history")
        assert "order-history" in driver.current_url

    def test_logout(self, driver, created_user):
        user_data, _ = created_user
        main_page = MainPage(driver)
        main_page.open_page("/")
        main_page.click_personal_account()

        login_page = LoginPage(driver)
        login_page.login(user_data["email"], user_data["password"])
        main_page.click_personal_account()

        profile_page = ProfilePage(driver)
        profile_page.click_logout()
        profile_page.wait_for_url("login")
        assert "login" in driver.current_url