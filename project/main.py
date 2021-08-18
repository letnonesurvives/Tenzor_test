import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from resources import TestData
from page_objects import HomePage, SearchResultPage
from resources import Locators
import os

os.environ['WDM_LOG_LEVEL'] = '0'

class WaitUntilNotElement(object):
    def __init__(self, element):
        self.element = element

    def __call__(self, driver):
        # Проверка на новый экз. элемента
        new_element = driver.find_element(*Locators.SEARCH_RESULT_FIRST_XPATH)
        new_element = new_element.find_element(*Locators.SEARCH_RESULT_FIRST_LINK).text
        if new_element == self.element:
            return new_element
        else:
            return False


class YandexTestCase(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--log-level=OFF")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        self.driver.implicitly_wait(30)

    def test_yandex_search(self) -> None:
        self.driver.get(TestData.BASE_URL)
        homepage = HomePage(self.driver)
        
        try:
            # Проверка доступности поля поиска
            is_search_available = homepage.is_visible(Locators.SEARCH_TEXT_INPUT)
        except:
            is_search_available = False

        if is_search_available:
            homepage.enter_search_text(TestData.SEARCH_TERM)

            try:
                # проверка на видимость таблицы
                is_suggest_table = homepage.is_visible(Locators.SUGGEST_TABLE)
            except:
                is_suggest_table = False

            # поиск
            homepage.press_return_key_search_field()

        self.assertTrue(is_search_available, "Search input is not available")
        self.assertTrue(is_suggest_table, "Suggest table is not visible")

        try:
            # Получение первого результата поиска
            search_result_page = SearchResultPage(homepage.driver)
            first_result_link = WebDriverWait(homepage.driver, 10).until(WaitUntilNotElement(TestData.TEST_ASSERT_URL))
        except:
            first_result_link = False

        self.assertTrue(first_result_link, f"First link is not equal to {TestData.TEST_ASSERT_URL}")

    def test_image_search_and_images_switch(self) -> None:
        self.driver.get(TestData.BASE_URL)
        homepage = HomePage(self.driver)

        try:
            # Проверка на видимость изображения
            is_image_link_btn = homepage.is_visible(Locators.IMAGE_LINK_BUTTON_XPATH)
        except:
            is_image_link_btn = False

        self.assertTrue(is_image_link_btn)

        # Перейти в картинки
        homepage.click(Locators.IMAGE_LINK_BUTTON_XPATH)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.implicitly_wait(5)

        # Клик на первую категорию
        homepage.click(Locators.FIRST_IMAGE_CATEGORY_LINK)
        self.driver.implicitly_wait(10)

        # Клик на первую картинку
        homepage.click(Locators.FIRST_IMAGE_LINK)

        # Проверка на всвпылвающее окно
        is_image_popup = homepage.is_visible(Locators.IMAGE_POPUP)
        self.assertTrue(is_image_popup,"image popup modal is not visible")

        next_image_btn = self.driver.find_element(*Locators.NEXT_IMAGE)
        previous_image_btn = self.driver.find_element(*Locators.PREVIOUS_IMAGE)

        previous_image = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.IMAGE_POPUP_SELECTED_ITEM))

        # Выполнить клик на кнопку следущее
        ActionChains(homepage.driver).move_to_element(next_image_btn).click().perform()
        next_image = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.IMAGE_POPUP_SELECTED_ITEM))
        self.assertNotEqual(previous_image, next_image)

        # Выполнить клик на кнопку предыдещее
        ActionChains(homepage.driver).move_to_element(previous_image_btn).click().perform()
        previous_image = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.IMAGE_POPUP_SELECTED_ITEM))

        # проверить что первая картинка не равна второй
        self.assertNotEqual(previous_image, next_image)

    def tearDown(self) -> None:
        super().tearDown()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()