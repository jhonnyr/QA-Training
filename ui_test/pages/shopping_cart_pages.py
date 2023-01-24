import time
from libraries import mapping, mouse, forms


class ShoppingCart:

    def __init__(self, driver):
        self.driver = driver
        self.item_button = "//a[contains(text(),'{}')]"
        self.add_car_button = "//a[contains(text(),'Add to cart')]"

    def click_on_product(self, product_name: str):
        mouse.click_on_element(self, "XPATH", self.item_button.format(product_name))

    def click_on_add_to_cart(self):
        mouse.click_on_element(self, "XPATH", self.add_car_button)

    def click
