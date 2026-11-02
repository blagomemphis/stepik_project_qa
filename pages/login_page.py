from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "URL не содержит 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.login_form), "Форма входа не найдена"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.reg_form), "Форма регистрации не найдена"

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()