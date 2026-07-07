from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://stellarburgers.education-services.ru"

    def open_page(self, url):
        self.driver.get(f"{self.base_url}{url}")

    def find_element_with_wait(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def wait_and_click(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        def attempt_click(driver):
            try:
                el = wait.until(EC.visibility_of_element_located(locator))
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
                wait.until(EC.element_to_be_clickable(locator)).click()
                return True
            except Exception:
                return False
        wait.until(attempt_click)

    def set_text_to_element(self, locator, text, timeout=10):
        element = self.find_element_with_wait(locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_text_from_element(self, locator, timeout=10):
        return self.find_element_with_wait(locator, timeout).text

    def check_element_is_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def drag_and_drop(self, source_locator, target_locator):
        source_element = self.find_element_with_wait(source_locator)
        target_element = self.find_element_with_wait(target_locator)
        js_script = """
        var source = arguments[0];
        var target = arguments[1];
        var dataTransfer = new DataTransfer();
        source.dispatchEvent(new DragEvent('dragstart', {bubbles: true, cancelable: true, dataTransfer: dataTransfer}));
        target.dispatchEvent(new DragEvent('dragenter', {bubbles: true, cancelable: true, dataTransfer: dataTransfer}));
        target.dispatchEvent(new DragEvent('dragover', {bubbles: true, cancelable: true, dataTransfer: dataTransfer}));
        target.dispatchEvent(new DragEvent('drop', {bubbles: true, cancelable: true, dataTransfer: dataTransfer}));
        source.dispatchEvent(new DragEvent('dragend', {bubbles: true, cancelable: true, dataTransfer: dataTransfer}));
        """
        self.driver.execute_script(js_script, source_element, target_element)

    def wait_for_url(self, url_part, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(url_part))