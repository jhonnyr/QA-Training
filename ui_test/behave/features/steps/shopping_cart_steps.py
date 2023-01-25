import os, allure
from allure_commons.types import AttachmentType
from behave import given, when, then

from ui_test.pages.shopping_cart_pages import ShoppingCart
from libraries.environment_setup import EnvironmentSetup

class LoginSteps(EnvironmentSetup):

    @when(u'Select the "{product_name}" item and add it to the shopping cart')
    def step_impl(context, product_name):

        context.shopping_cart = ShoppingCart(context.driver)
        context.shopping_cart.click_on_product(product_name)
        allure.attach(context.driver.get_screenshot_as_png(), name="Item_Selected.png", attachment_type=AttachmentType.PNG)
        context.shopping_cart.click_on_add_to_cart()

    @then(u'Go to the shopping car and buy the item')
    def step_impl(context):
        context.shopping_cart.click_on_car_option()
        allure.attach(context.driver.get_screenshot_as_png(), name="Cart Option.png", attachment_type=AttachmentType.PNG)
        context.shopping_cart.place_order_option()
        allure.attach(context.driver.get_screenshot_as_png(), name="Place Order Option.png", attachment_type=AttachmentType.PNG)
        for row in context.table:
            context.name = row["name"]
            context.country = row["country"]
            context.city = row["city"]
            context.credit_card = row["credit_card"]
            context.month = row["month"]
            context.year = row["year"]
        context.shopping_cart.purchase(context.name, context.country, context.city, context.credit_card, context.month, context.year)
        allure.attach(context.driver.get_screenshot_as_png(), name="Purchase.png",
                      attachment_type=AttachmentType.PNG)
