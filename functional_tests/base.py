from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import sys
from selenium import webdriver

class FunctionalTest(StaticLiveServerTestCase):
    # @classmethod
    # def setUpClass(cls):
    #     for arg in sys.argv:
    #         if 'liveserver' in arg:
    #             cls.server_url = 'http://' + arg.split('=')[1]
    #             return
    #     super().setUpClass()
    #     cls.server_url = cls.live_server_url

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

