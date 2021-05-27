from flask import url_for
from flask_testing import TestCase
import requests_mock
from application import app

class TestBase(TestBase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_get_animal(self):
        for _ in range(20):
            response = self.client.get(url_for('get_animal'))
            self.assertIn(response.data.decode("utf-8"),["cow", "pig", "horse"])
# with patch() as :
#             r.return_value='cow'
#         response = self.client.get(url_for('get_animal'))
#         self.asserEqual(response.status_code, 200)
#         self.assertIm(b'cow', response.data)
class TestHome(TestBase):
    def test_get_noise(self):
        test_cases = [("cow", "moo"), ("pig","oink"), ("horse", "neigh")]
        for case in test_case:
             response = self.client.get(url_for('get_noise'), data=case[0])
             self.assertIn(response.data.decode("utf-8"), case[1])


        # with requests_mock.Mocker() as mocker:
        #     mocker.get('http://animal_noises_api:5000/get_animal', text='duck')
        #     mocker.post('http://animal_noises_api:5000/get_noise', text= 'quack')
        #  response = self.client.get(url_for('home'))
        # self.asserEqual(response.status_code, 200)
        # self.assertIm(b'The duck goes quack', response.data)

 