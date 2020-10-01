from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from requests import get, post


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
        assert 'To-Do' in self.selenium.title
        # print(self.selenium.title)

    def test_description(self):
        """User reads a description of the site and sees a link for the project repo"""
        body = self.selenium.find_element_by_tag_name("body")
        print(dir(body))
        assert 'This is the landing page for a to-do list api' in body.text
        assert 'https://github.com/JonathanFrederick/todo-api/' in \
            body.find_element_by_tag_name('a').get_property('href')

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

class UserCreationTestClass(LiveServerTestCase):
    username = "Simon_Tam"
    password = "mei-mei123"
    email = "stam000@UOsiris.edu"

    def test_correct_user_registration(self):
        register_body = {
            "username": self.username,
            "email": self.email,
            "password": self.password
        }
        register_resp = post(f"{self.live_server_url}/registration",
            register_body)
        assert register_resp.status_code == 201

    # def test_correct_user_login(self):
    #     login_body={
    #         "email": email,
    #         "password": password
    #     }
    #     login_resp = get(f"{self.live_server_url}/login", login_body)
    #     assert login_resp.status_code == 200
