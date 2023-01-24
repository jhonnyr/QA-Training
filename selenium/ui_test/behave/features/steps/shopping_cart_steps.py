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
        allure.attach(context.driver.get_screenshot_as_png(), name="Item Selected.png", attachment_type=AttachmentType.PNG)
        context.shopping_cart.add_car_button()
        allure.attach(context.driver.get_screenshot_as_png(), name="Add cart.png", attachment_type=AttachmentType.PNG)

    @then(u'Buy the item')
    def step_impl (context):

        context.shopping_cart.
