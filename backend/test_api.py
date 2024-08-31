import unittest

from base import api

class TestApi(unittest.TestCase):
    def setUp(self):
        self.client = api.test_client()

    def test_add(self):
        response = self.client.post("/add", data={"num1": "1", "num2": "2"})
        assert response.status_code == 200
        assert response.json["data"]["answer"] == 3

    def test_subtract(self):
        response = self.client.post("/subtract", data={"num1": "1", "num2": "2"})
        assert response.status_code == 200
        assert response.json["data"]["answer"] == -1

    def test_empty_fields(self):
        response = self.client.post("/add", data={"num1": "", "num2": ""})
        assert response.status_code == 200
        assert response.json["data"]["answer"] == 0

    def test_whitespace(self):
        response = self.client.post("/add", data={"num1": " ", "num2": "2"})
        assert response.status_code == 200
        assert response.json["data"]["answer"] == 2

    def test_error(self):
        response = self.client.post("/subtract", data={"num1": "a", "num2": "2"})
        assert response.status_code == 400
        assert response.json["error"] == "Invalid value given. Please only input numbers."

if __name__ == "__main__":
    unittest.main()