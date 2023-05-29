from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_ITEMS), "Basket items are present, but should not be"
    def should_display_empty_basket_text(self):
        empty_basket_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text
        assert "Ваша корзина пуста" in empty_basket_text, "Empty basket text is not displayed"

