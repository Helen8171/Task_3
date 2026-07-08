import allure
from pages.base_page import BasePage
from locators.locators import FeedPageLocators

class FeedPage(BasePage):
    @allure.step("Клик по первому заказу в ленте")
    def click_on_order(self):
        self.wait_and_click(FeedPageLocators.ORDER_ITEM)

    @allure.step("Проверка открытия модального окна заказа")
    def check_order_modal_opened(self):
        return self.check_element_is_visible(FeedPageLocators.ORDER_MODAL)

    @allure.step("Получение количества заказов за все время")
    def get_total_orders_count(self):
        return self.get_text_from_element(FeedPageLocators.TOTAL_ORDERS_COUNTER)

    @allure.step("Получение количества заказов за сегодня")
    def get_today_orders_count(self):
        return self.get_text_from_element(FeedPageLocators.TODAY_ORDERS_COUNTER)

    @allure.step("Получение списка заказов в работе")
    def get_orders_in_progress(self):
        return self.get_text_from_element(FeedPageLocators.ORDERS_IN_PROGRESS)

    @allure.step("Ожидание изменения счетчика заказов за все время")
    def wait_for_total_orders_change(self, initial_count):
        self.wait_until_text_changes(FeedPageLocators.TOTAL_ORDERS_COUNTER, initial_count)

    @allure.step("Ожидание изменения счетчика заказов за сегодня")
    def wait_for_today_orders_change(self, initial_count):
        self.wait_until_text_changes(FeedPageLocators.TODAY_ORDERS_COUNTER, initial_count)