from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from .main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
class ProductPage(BasePage):
    def can_add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()
    # метод проверки совпадения названия товара в карточке с названием товара в корзине
    def should_be_message_name_product(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_NAME).text, "В корзину добавился не тот товар"
    # метод проверки совпадения цены товара в карточке с ценой товара в корзине
    def should_be_massage_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == self.browser.find_element(*ProductPageLocators.BASKET_PRICE_NAME).text, "Цена товара не совападает"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
