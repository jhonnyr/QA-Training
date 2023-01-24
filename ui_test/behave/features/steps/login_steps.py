import os, allure
from allure_commons.types import AttachmentType
from behave import given, when, then

from libraries import mapping
from ui_test.pages.login_page import Login
from libraries.environment_setup import EnvironmentSetup

class LoginSteps(EnvironmentSetup):

    @given(u'As user login to the admin application in the environment')
    def step_impl(context):

        context.url = mapping.map_environment()
        context.driver.get(context.url)
        context.login = Login(context.driver)
        context.login.load()
        context.login.click_on_log_in_button()
        username = os.environ.get("USER_NAME")
        password = os.environ.get("PASSWORD")
        context.login.type_user_name(username)
        context.login.type_password(password)
        context.login.click_on_sign_in_button()
        allure.attach(context.driver.get_screenshot_as_png(), name="Goto_Login.png", attachment_type=AttachmentType.PNG)

