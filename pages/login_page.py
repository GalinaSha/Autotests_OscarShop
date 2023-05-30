from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # Проверка на корректный url адрес
        assert "login" in self.browser.current_url, "Substring 'login' is not present in the current URL"

    def should_be_login_form(self):
        # Проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present on the page"

    def should_be_register_form(self):
        # Проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present on the page"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_INPUT)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_INPUT)
        password_input.send_keys(password)
        confirm_password_input = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD_INPUT)
        confirm_password_input.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()