from unittest import TestCase
from selenium import webdriver


class LandingPageTestClass(TestCase):
    @classmethod
    def setUpClass(cls):
        """User vists the homepage"""
        cls.browser = webdriver.Firefox()
        cls.browser.get("http://localhost:8000")
    
    def test_title(self):
        """User notices a somewhat descriptive title"""
        assert 'To-Do' in self.browser.title

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()