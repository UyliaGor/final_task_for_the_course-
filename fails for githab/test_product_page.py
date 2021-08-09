
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from selenium.webdriver.support import expected_conditions as EC
import time
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.can_add_product_to_basket()
    print(page.solve_quiz_and_get_code())
    page.should_be_message_name_product()
    page.should_be_massage_price()
