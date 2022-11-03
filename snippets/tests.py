from urllib import request, response
from django.test import TestCase

# Create your tests here.

class TopPageViewTest(TestCase):
    def test_top_returns_200(self):
        # HttpRequestオブジェクトの作成
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_top_returns_expected_content(self):
        # HttpRequestオブジェクトの作成
        response = self.client.get('/')
        self.assertEqual(response.content, b'Hello World')