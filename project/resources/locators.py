from selenium.webdriver.common.by import By

class Locators(object):
    SEARCH_TEXT_INPUT = (By.NAME, "text")
    SUGGEST_TABLE = (By.CLASS_NAME, "mini-suggest__popup")
    SEARCH_RESULT = (By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[1]/div[1]/ul/li[1]')
    SEARCH_RESULT_FIRST_XPATH = (By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[1]/div[1]/ul/li[1]')
    SEARCH_RESULT_FIRST_LINK = (By.CLASS_NAME, "link.path__item")
    IMAGE_LINK_BUTTON_XPATH = (By.XPATH, "/html/body/div[1]/div[2]/div[3]/div/div[2]/nav/div/ul/li[3]/a")
    FIRST_IMAGE_CATEGORY_LINK = (By.XPATH, "/html/body/div[4]/div[1]/div[1]/div/div/div[1]/a")
    FIRST_IMAGE_LINK = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/div[1]/div/div[1]/div/a')
    IMAGE_POPUP_SELECTED_ITEM = (By.CLASS_NAME, "MMGallery-Item.MMGallery-Item_selected")
    IMAGE_POPUP = (By.CLASS_NAME, "Popup2")
    NEXT_IMAGE = (By.CLASS_NAME, "CircleButton_type_next")
    PREVIOUS_IMAGE = (By.CLASS_NAME, "CircleButton_type_prev")