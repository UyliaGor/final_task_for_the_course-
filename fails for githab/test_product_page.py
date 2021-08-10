import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

def test_guest_can_add_product_to_basket(browser,link):
    page = ProductPage(browser, link)
    page.open()                      # открываем страницу
    page.can_add_product_to_basket()
    print(page.solve_quiz_and_get_code())
    page.should_be_message_name_product()
    page.should_be_massage_price()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
   link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
                      # открываем страницу
   page = ProductPage(browser,link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
   page.open()
   page.can_add_product_to_basket()
   page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
   link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
                      # открываем страницу
   page = ProductPage(browser,link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
   page.open()
   page.should_not_be_success_message()
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
   link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
                      # открываем страницу
   page = ProductPage(browser,link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
   page.open()
   page.can_add_product_to_basket()
   page.should_disappear_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url) #переход между страницами
    login_page.should_be_login_page()

