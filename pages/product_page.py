from .base_page import BasePage
from .locators import ItemPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_cart_btn = self.browser.find_element(*ItemPageLocators.ADD_CART_BTN)
        add_to_cart_btn.click()

    def verify_success_messages(self):
        product_name = self.get_text(ItemPageLocators.PRODUCT_NAME)
        success_message = self.get_text(ItemPageLocators.SUCCESS_MESSAGE)
        assert product_name == success_message, "Имя товара в сообщении об успешном добавлении не совпадает"

    def verify_basket_total(self):
        product_price = self.get_text(ItemPageLocators.PRODUCT_PRICE)
        basket_total = self.get_text(ItemPageLocators.BASKET_TOTAL)
        assert product_price == basket_total, "Общая сумма корзины не совпадает с ценой товара"

    def get_text(self, locator):
        element = self.browser.find_element(*locator)
        return element.text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ItemPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ItemPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

