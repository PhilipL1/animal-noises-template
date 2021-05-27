from flask import url_for
from flask_testing import TestCase
import requests_mock
from application import app

class TestBase(TestBase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_home(self):
        with requests_mock.Mocker() as mocker:
            mocker.get('http://animal_noises_api:5000/get_animal', text='duck')
            mocker.post('http://animal_noises_api:5000/get_noise', text= 'quack')
        response = self.client.get(url_for('home'))
        self.asserEqual(response.status_code, 200)
        self.assertIm(b'The duck goes quack', response.data)

 