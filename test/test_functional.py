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

    def test_description(self):
        """User reads a description of the site and sees a link for the project repo"""
        body = self.browser.find_element_by_tag_name("body").text
        assert 'This is the landing page for a to-do list api' in body
        assert 'https://github.com/JonathanFrederick/todo-api/' in body

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()