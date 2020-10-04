from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.contrib.auth.models import User
from api.views import register


class RegistrationEndPointTest(TestCase):
    username = "mal"
    email = "mreynolds@browncoats.mil"
    password = "7pinespass"

    def test_registration_url_resolves_to_register_view(self):
        found = resolve('/registration')
        self.assertEqual(found.func, register)

    def test_correct_registration_url_request(self):
        body = {
            "username": self.username,
            "email": self.email,
            "password": self.password,
        }
        response = self.client.post('/registration', data=body)
        self.assertEqual(response.status_code, 201)

        user = User.objects.get(username=self.username)
        self.assertTrue(user, msg="User came back as None/False")

    def test_registration_error_with_GET(self):
        request = HttpRequest()
        request.method = 'GET'
        response = register(request)
        self.assertTrue(response.status_code > 399)
