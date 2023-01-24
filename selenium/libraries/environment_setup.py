import unittest

from libraries import selenium_env


class EnvironmentSetup(unittest.TestCase):
    def setUp(self):
        self.driver = selenium_env.createEnvironment()
        self.driver.maximize_window()
        return self.driver

    def tearDown(self):
        self.driver.quit()
