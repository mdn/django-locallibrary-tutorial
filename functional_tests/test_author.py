from .base import FunctionalTest

class TestHomepage(FunctionalTest):

    def test_home(self):
        self.browser.get(self.live_server_url + '/catalog/authors')
        self.assertEqual(self.browser.title, 'Local Library')
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertEqual(header_text, 'Author List')
