from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from resources import Locators

class HomePage:
    
    def __init__(self, driver) -> None:
        self.driver = driver
    
    # выполнить клик по локатору по элементу
    def click(self, by_locator) -> object:
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()
        return element

    # Проверка на видимость
    def is_visible(self, by_locator) -> bool:
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    # Ввод текста для поиска
    def enter_search_text(self, text) -> object:
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.SEARCH_TEXT_INPUT)).send_keys(text)

    # Выполнить поиск
    def press_return_key_search_field(self) -> object:
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.SEARCH_TEXT_INPUT)).send_keys(Keys.ENTER)