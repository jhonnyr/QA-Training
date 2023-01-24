import unittest

from libraries import selenium_env_local


class EnvironmentSetup(unittest.TestCase):
    def setUp(self):
        self.driver = selenium_env_local.createEnvironment()
        self.driver.maximize_window()
        return self.driver

    def tearDown(self):
        self.driver.quit()
