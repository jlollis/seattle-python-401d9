import unittest


class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from weather_api import main
        app = main({})
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_root_status_200(self):
        res = self.testapp.get('/', status=200)
        self.assertTrue(res.status_code, 200)

    def test_root_content(self):
        res = self.testapp.get('/', status=200)
        self.assertIn('GET / - Base API route', res.text)

    def test_GET_one_weather_status_200(self):
        res = self.testapp.get('/api/v1/weather/1/', status=200)
        self.assertTrue(res.status_code, 200)

    def test_GET_all_weather_status_200(self):
        res = self.testapp.get('/api/v1/weather/', status=200)
        self.assertTrue(res.status_code, 200)

    def test_POST_weather_status_201(self):
        res = self.testapp.post('/api/v1/weather/', status=201)
        self.assertTrue(res.status_code, 201)

    def test_DELETE_weather_status_204(self):
        res = self.testapp.delete('/api/v1/weather/1/', status=204)
        self.assertTrue(res.status_code, 204)

    def test_GET_login_status_200(self):
        res = self.testapp.get('/api/v1/auth/', status=200)
        self.assertTrue(res.status_code, 200)

    def test_POST_register_status_201(self):
        res = self.testapp.post('/api/v1/auth/', status=201)
        self.assertTrue(res.status_code, 201)
