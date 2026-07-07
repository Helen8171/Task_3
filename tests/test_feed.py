from pages.main_page import MainPage
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait

class TestFeed:
    def test_click_order_opens_modal(self, driver):
        feed_page = FeedPage(driver)
        feed_page.open_page("/feed")
        feed_page.click_on_order()
        assert feed_page.check_order_modal_opened()

    def test_new_order_increases_total_counter(self, driver, created_user):
        user_data, _ = created_user
        feed_page = FeedPage(driver)
        feed_page.open_page("/feed")
        initial_count = feed_page.get_total_orders_count()

        main_page = MainPage(driver)
        main_page.open_page("/")
        main_page.click_personal_account()
        login_page = LoginPage(driver)
        login_page.login(user_data["email"], user_data["password"])
        main_page.add_ingredient_to_order()
        main_page.click_order_button()
        main_page.check_order_modal_opened()
        main_page.close_modal()

        feed_page.open_page("/feed")
        WebDriverWait(driver, 10).until(lambda d: feed_page.get_total_orders_count() != initial_count)
        new_count = feed_page.get_total_orders_count()
        assert int(new_count) > int(initial_count)

    def test_new_order_increases_today_counter(self, driver, created_user):
        user_data, _ = created_user
        feed_page = FeedPage(driver)
        feed_page.open_page("/feed")
        initial_count = feed_page.get_today_orders_count()

        main_page = MainPage(driver)
        main_page.open_page("/")
        main_page.click_personal_account()
        login_page = LoginPage(driver)
        login_page.login(user_data["email"], user_data["password"])
        main_page.add_ingredient_to_order()
        main_page.click_order_button()
        main_page.check_order_modal_opened()
        main_page.close_modal()

        feed_page.open_page("/feed")
        WebDriverWait(driver, 10).until(lambda d: feed_page.get_today_orders_count() != initial_count)
        new_count = feed_page.get_today_orders_count()
        assert int(new_count) > int(initial_count)