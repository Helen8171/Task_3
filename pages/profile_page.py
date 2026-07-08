import allure
from pages.base_page import BasePage
from locators.locators import ProfilePageLocators

class ProfilePage(BasePage):
    @allure.step("Клик по ссылке 'История заказов'")
    def click_order_history(self):
        self.wait_and_click(ProfilePageLocators.ORDER_HISTORY_LINK)

    @allure.step("Клик по кнопке выхода")
    def click_logout(self):
        self.wait_and_click(ProfilePageLocators.LOGOUT_BUTTON)