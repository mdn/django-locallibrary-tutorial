from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import sys
from selenium import webdriver

class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

