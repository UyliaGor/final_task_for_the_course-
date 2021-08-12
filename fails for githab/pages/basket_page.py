from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException # в начале файла
import math
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from .main_page import MainPage
from .locators import BasketPageLocators


class BasketPage(BasePage):
   def sould_be_empty_basket(self):
      assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT) == True , "Products in the basket "

   def sould_be_empty_basket_message(self):
      assert self.is_element_present(*BasketPageLocators.BASKET_TEXT) == True, "Message Your basket is NOT empty"
