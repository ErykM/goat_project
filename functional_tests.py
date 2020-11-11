import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    """
    Basic test class
    """
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_list_and_retrieve_it_later(self):
        # User checks if webapp opens
        self.browser.get('http://localhost:8000')

        # User checks if title has to-do in it
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
