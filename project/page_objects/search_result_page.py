from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from resources import Locators

class SearchResultPage:
    def __init__(self, driver):
        self.driver = driver

    # Получить атрибут href ссылки
    def get_link_href(self, by_locator) -> str:
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).find_element(*Locators.SEARCH_RESULT_FIRST_LINK).get_attribute("href")
        return element
