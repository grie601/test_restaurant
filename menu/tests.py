# Create your tests here.
import django.contrib.sites.requests
from django.test import TestCase
from menu.forms import AddDish
import requests

class MyTests(TestCase):
    def test_forms(self):
        post_url = 'http://127.0.0.1:8000/api/dish/dishes/'
        files = {
            "image": open("3.png", 'rb')}
        form_data = {'name_dish': 'Шашлык', "nutrition_value": "250", "value": "600"}
        r = requests.post(post_url, data=form_data, files=files)
        form = AddDish(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(r.status_code, 200)
