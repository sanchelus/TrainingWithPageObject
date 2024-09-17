from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_into_basket(self):
        product_name = self.get_product_name()
        product_price = self.get_product_price()
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        link.click()
        self.solve_quiz_and_get_code()
        self.should_be_product_name(product_name)
        self.should_be_product_price(product_price)

    def add_product_into_basket_without_any_checks(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        link.click()
        self.solve_quiz_and_get_code()

    def get_product_name(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE)
        return name.text

    def get_product_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return price.text

    def should_be_product_name(self, name_product):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET_NAME)
        name_in_basket = name.text
        assert name_product == name_in_basket, f"Added in basket another product {name_product}!=={name_in_basket}"

    def should_be_product_price(self, product_price):
        price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        price_in_basket = price.text
        assert product_price == price_in_basket, \
            f"Added in basket price not equals to product price{product_price}!={price_in_basket}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_IN_BASKET_NAME), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_IN_BASKET_NAME), \
            "Success message is not disappeared, but should be"