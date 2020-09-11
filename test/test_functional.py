from unittest import TestCase
from selenium import webdriver


class TestClass(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Firefox()
        cls.browser.get("http://localhost:8000")

    def test_smoke(self):
        assert True
    
    def test_title(self):
        assert 'Django' in self.browser.title

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()