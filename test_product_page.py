from pages.locators import ProductPageLocators
from pages.product_page import ProductPage
from pages.login_page import LoginPage
import pytest
import time

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Сообщение появилось, но не должно было"

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Сообщение появилось, но не должно было"

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = f"test_{int(time.time())}@example.com"
        password = "StrongPass123!"
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        assert page.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "Сообщение появилось, но не должно было"

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.should_be_add_to_basket_message()
        page.should_be_basket_total_price()