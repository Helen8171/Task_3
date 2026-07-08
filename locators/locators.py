from selenium.webdriver.common.by import By

class MainPageLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, ".//p[text()='Лента Заказов']")
    BUN_INGREDIENT = (By.XPATH, ".//a[contains(@class, 'BurgerIngredient_ingredient')]")
    INGREDIENT_COUNTER = (By.XPATH, ".//a[contains(@class, 'BurgerIngredient_ingredient')]//p[contains(@class, 'counter_counter__num')]")
    INGREDIENT_DETAILS_HEADER = (By.XPATH, ".//h2[text()='Детали ингредиента']")
    CLOSE_MODAL_BUTTON = (By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]//button[contains(@class, 'Modal_modal__close')]")
    ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
    BASKET_DROP_ZONE = (By.XPATH, ".//section[contains(@class, 'BurgerConstructor_basket')]")

class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    FORGOT_PASSWORD_LINK = (By.XPATH, ".//a[text()='Восстановить пароль']")

class ForgotPasswordLocators:
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    RESTORE_BUTTON = (By.XPATH, ".//button[text()='Восстановить']")
    PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")
    SHOW_PASSWORD_ICON = (By.XPATH, ".//div[contains(@class, 'input__icon')]")
    ACTIVE_PASSWORD_FIELD = (By.XPATH, ".//div[contains(@class, 'input_status_active')]")

class ProfilePageLocators:
    ORDER_HISTORY_LINK = (By.XPATH, ".//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")

class FeedPageLocators:
    ORDER_ITEM = (By.XPATH, ".//a[contains(@href, '/feed/')][1]")
    ORDER_MODAL = (By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]")
    TOTAL_ORDERS_COUNTER = (By.XPATH, ".//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_ORDERS_COUNTER = (By.XPATH, ".//p[text()='Выполнено за сегодня:']/following-sibling::p")
    ORDERS_IN_PROGRESS = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady')]/li")