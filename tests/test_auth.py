import json

import pytest
from fastapi.testclient import TestClient

from main import app


class TestAuth:
    def setup(self):
        self.client = TestClient(app)

    @pytest.fixture()
    def user_data(self):
        return {
            "first_name": "Boris",
            "email": "asd@secret.ru",
            "password": "secret",
            "timezone": 3
        }

    @pytest.fixture()
    def login_data(self):
        return {
            "email": "asd@secret.ru",
            "password": "secret"
        }

    def test_validate_signup(self):
        response_first_name = self.client.post("/api/v1/user/signup", data={
            "email": "asd@asd.ru",
            "password": "secret",
            "timezone": 3
        })

        response_email = self.client.post("/api/v1/user/signup", data={
            "first_name": "Boris",
            "email": "asd@",
            "password": "secret",
            "timezone": 3
        })

        response_empty_password = self.client.post("/api/v1/user/signup", data={
            "first_name": "Boris",
            "email": "asd@",
            "timezone": 3
        })

        response_empty_timezone = self.client.post("/api/v1/user/signup", data={
            "first_name": "Boris",
            "email": "asd@",
            "password": "secret",
        })

        assert response_first_name.status_code == 422
        assert response_email.status_code == 422
        assert response_empty_password.status_code == 422
        assert response_empty_timezone.status_code == 422

    def test_signup(self, user_data):
        response_signup = self.client.post("/api/v1/user/signup", data=json.dumps(user_data))

        assert response_signup.status_code == 200
        data = response_signup.json()
        assert data["status"] == 'Success'
        assert bool(data["access_token"]) == True

    def test_login(self, login_data):
        response_login = self.client.post("/api/v1/user/login",
                                          data=json.dumps(login_data))

        assert response_login.status_code == 200
        data = response_login.json()
        assert bool(data["access_token"]) == True
