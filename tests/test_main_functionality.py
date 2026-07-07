from pages.main_page import MainPage
from pages.login_page import LoginPage


class TestMainFunctionality:
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open_page("/login")
        main_page.click_constructor()
        main_page.wait_for_url("/")
        assert driver.current_url == f"{main_page.base_url}/"

    def test_go_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open_page("/")
        main_page.click_order_feed()
        main_page.wait_for_url("feed")
        assert "feed" in driver.current_url

    def test_ingredient_modal_opens(self, driver):
        main_page = MainPage(driver)
        main_page.open_page("/")
        main_page.click_ingredient()
        assert main_page.check_ingredient_details_opened()

    def test_close_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_page("/")
        main_page.click_ingredient()
        main_page.close_modal()
        assert True

    def test_add_ingredient_increases_counter(self, driver):
        main_page = MainPage(driver)
        main_page.open_page("/")
        main_page.add_ingredient_to_order()
        counter = main_page.get_ingredient_counter()
        assert counter == "2"

    def test_logged_in_user_can_order(self, driver, created_user):
        user_data, _ = created_user
        main_page = MainPage(driver)
        main_page.open_page("/")
        main_page.click_personal_account()

        login_page = LoginPage(driver)
        login_page.login(user_data["email"], user_data["password"])

        main_page.add_ingredient_to_order()
        main_page.click_order_button()
        assert main_page.check_order_modal_opened()