# project: Divisors
# author: Lukasz Kostrzewa

from django.test import SimpleTestCase
from django.test import Client
from django.test.utils import setup_test_environment

class WebappTest(SimpleTestCase):
    """
    Django tests. Check if the divisors site returns proper
    response for the given requests.
    """

    def setUp(self):
        self.client = Client()
        
        #throws error when initialized more than once
        try:
            setup_test_environment()
        except(RuntimeError):
            pass


    def test_no_number(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "initialize_divisors([], 0)")

    def test_25(self):
        response = self.client.post('/', {'number': 25})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "divisor3")
        self.assertContains(response, "divisors of 25")     