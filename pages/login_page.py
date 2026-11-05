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

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.reg_email)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.reg_password)
        password_field.send_keys(password)
        confirm_field = self.browser.find_element(*LoginPageLocators.confirm_password)
        confirm_field.send.keys(password)
        submit_button = self.browser.find_element(*LoginPageLocators.reg_button)
        submit_button.click()