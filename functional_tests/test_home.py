from .base import FunctionalTest

class TestHomepage(FunctionalTest):

    def test_home(self):
        self.browser.get(self.live_server_url)
        self.assertEqual(self.browser.title, 'Local Library')
