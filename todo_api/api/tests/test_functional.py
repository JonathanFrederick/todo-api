# from unittest import TestCase
from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver


class LandingPageTestClass(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        """User vists the homepage"""
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)
        # cls.selenium.get("http://localhost:8000")
        cls.selenium.get(cls.live_server_url)
        
        
    
    def test_title(self):
        """User notices a somewhat descriptive title"""
        # assert 'To-Do' in self.selenium.title
        print(self.selenium.title)

    def test_description(self):
        """User reads a description of the site and sees a link for the project repo"""
        body = self.selenium.find_element_by_tag_name("body").text
        assert 'This is the landing page for a to-do list api' in body
        assert 'https://github.com/JonathanFrederick/todo-api/' in body

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()
