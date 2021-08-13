from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
    LOGIN_FORM = (By.CLASS_NAME,'login_form')
    REGISTER_FORM = (By.CLASS_NAME,'register_form')
    EMAIL_ADRESS = (By.CSS_SELECTOR, "[id=id_registration-email]")
    PASSWORD_1 = (By.CSS_SELECTOR, "[id=id_registration-password1]")
    PASSWORD_2 = (By.CSS_SELECTOR, "[id=id_registration-password2]")
    BUTTON_REGISTER = (By.CSS_SELECTOR, "[name=registration_submit]")
class ProductPageLocators():
    BASKET_BUTTON = (By.CLASS_NAME,'btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, " .alert:nth-child(1) strong")
    BASKET_PRICE_NAME = (By.CSS_SELECTOR, ".alert:nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert:nth-child(1)")
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CLASS_NAME, "btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
class BasketPageLocators():
    BASKET_TEXT = (By.CSS_SELECTOR, "[id = content_inner]>p")
    BASKET_PRODUCT = (By.CLASS_NAME, ".hidden-xs")
