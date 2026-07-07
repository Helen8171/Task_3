from pages.base_page import BasePage
from locators.locators import FeedPageLocators


class FeedPage(BasePage):
    def click_on_order(self):
        self.wait_and_click(FeedPageLocators.ORDER_ITEM)

    def check_order_modal_opened(self):
        return self.check_element_is_visible(FeedPageLocators.ORDER_MODAL)

    def get_total_orders_count(self):
        return self.get_text_from_element(FeedPageLocators.TOTAL_ORDERS_COUNTER)

    def get_today_orders_count(self):
        return self.get_text_from_element(FeedPageLocators.TODAY_ORDERS_COUNTER)

    def get_orders_in_progress(self):
        return self.get_text_from_element(FeedPageLocators.ORDERS_IN_PROGRESS)