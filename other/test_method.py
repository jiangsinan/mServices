from unittest import TestCase
import requests


class TestTornadoRequest(TestCase):
    base_url = 'http://localhost:8000'

    def test_index_post(self):
        url = self.base_url + '/'
        resp = requests.post(url, data={
            'name': 'jsn',
            'city': '西安'
        })
        print(resp.text)


class TestCookieRequest(TestCase):
    base_url = 'http://localhost:8000/cookie'

    def test_get(self):
        resp = requests.get(self.base_url)
        print(resp.text)

    def test_delete(self):
        resp = requests.delete(self.base_url, params={
            'name': 'token'
        })
        print(resp.text)

class TestLoginRequest(TestCase):
    base_url = 'http://localhost:8000/login'
    def test_login_get(self):
        resp = requests.get(self.base_url,json={
            'name':'yky',
            'pwd':'123456',
        })
        print(resp.text)