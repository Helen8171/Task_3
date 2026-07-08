import allure
from pages.base_page import BasePage
from locators.locators import MainPageLocators
from locators.locators import FeedPageLocators

class MainPage(BasePage):
    @allure.step("Клик по кнопке 'Личный Кабинет'")
    def click_personal_account(self):
        self.wait_and_click(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Клик по кнопке 'Конструктор'")
    def click_constructor(self):
        self.wait_and_click(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Клик по кнопке 'Лента Заказов'")
    def click_order_feed(self):
        self.wait_and_click(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Клик по ингредиенту")
    def click_ingredient(self):
        self.wait_and_click(MainPageLocators.BUN_INGREDIENT)

    @allure.step("Проверка открытия деталей ингредиента")
    def check_ingredient_details_opened(self):
        return self.check_element_is_visible(MainPageLocators.INGREDIENT_DETAILS_HEADER)

    @allure.step("Закрытие модального окна")
    def close_modal(self):
        self.wait_and_click(MainPageLocators.CLOSE_MODAL_BUTTON)

    @allure.step("Добавление ингредиента в корзину")
    def add_ingredient_to_order(self):
        self.drag_and_drop(MainPageLocators.BUN_INGREDIENT, MainPageLocators.BASKET_DROP_ZONE)

    @allure.step("Получение счетчика ингредиента")
    def get_ingredient_counter(self):
        return self.get_text_from_element(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step("Клик по кнопке оформления заказа")
    def click_order_button(self):
        self.wait_and_click(MainPageLocators.ORDER_BUTTON)

    @allure.step("Проверка открытия модального окна заказа")
    def check_order_modal_opened(self):
        return self.check_element_is_visible(FeedPageLocators.ORDER_MODAL)