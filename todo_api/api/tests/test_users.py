from django.test import TestCase
from django.urls import resolve
from api.views import register
from django.http import HttpRequest

class RegistrationEndPointTest(TestCase):
    def test_registration_url_resolves_to_register_view(self):
        found = resolve('/registration')
        self.assertEqual(found.func, register)

    def test_correct_registration_url_request(self):
        request = HttpRequest()
        request.method = 'POST'
        response = register(request)
        self.assertEqual(response.status_code, 201)
    
    def test_registration_error_with_GET(self):
        request = HttpRequest()
        request.method = 'GET'
        response = register(request)
        self.assertTrue(response.status_code > 399 )

    
