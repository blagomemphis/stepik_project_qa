from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()  # ← решает alert автоматически

    def should_be_add_to_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Сообщение о добавление товара не найдено"
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        name_in_message = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_MESSAGE
        ).text
        assert product_name == name_in_message, \
            f"Название товара не совпадает: {product_name} != {name_in_message}"

    def should_be_basket_total_price(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL_MESSAGE), \
            "Сообщение о стоимости корзины не найдено"
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE).text
        # нормализация: "9,99 £" → 9.99, "£9.99" → 9.99
        price = float(product_price.replace("£", "").replace(",", ".").replace(" ", "").replace("\xa0", ""))
        total = float(basket_total.replace("£", "").replace(",", ".").replace(" ", "").replace("\xa0", ""))
        assert price == total, \
            f"Стоимость корзины не совпадает: {price} != {total}"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Сообщение отобразилось, но должно было исчезнуть"
