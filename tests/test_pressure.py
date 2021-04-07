import json

import pytest
from fastapi import Depends
from fastapi.testclient import TestClient

from core.db import get_db, SessionLocal
from main import app
from models.statistics_pressure import StatisticsPressure
from models.user import User
from utills.delete_all_data_user import delete_all_data_user


class TestPressure:
    id_one_row = None


    def setup(self,):
        self.client = TestClient(app)
        response_auth = self.client.post("/api/v1/user/login", data=json.dumps(
            {
                "email": "asd@secret.ru",
                "password": "secret"
            }
        ))
        response = response_auth.json()

        self.token = {'Authorization': 'Bearer ' + response["access_token"]}


    def teardown_class(cls):
        delete_all_data_user(email="asd@secret.ru")


    @pytest.fixture()
    def pressue_origin_data(self):
        return {
            "upper": 120,
            "down": 80,
            "heartbeat": 80,
            "timezone": 3
        }

    @pytest.fixture()
    def pressue_updated_data(self):
        return {
            "upper": 1200,
            "down": 1800,
            "heartbeat": 800,
            "timezone": 3
        }


    def test_add_pressure(self, pressue_origin_data):
        response_pressure = self.client.post("/api/v1/pressure/add",
                                             headers=self.token,
                                             data=json.dumps(pressue_origin_data))
        response_pressure_2 = self.client.post("/api/v1/pressure/add",
                                             headers=self.token,
                                             data=json.dumps(pressue_origin_data))

        response_pressure_empty_optional = self.client.post("/api/v1/pressure/add",
                                                            headers=self.token,
                                                            data={
                                                                "upper": 120,
                                                                "down": 80,
                                                            })

        response_pressure_empty_upper = self.client.post("/api/v1/pressure/add",
                                                         headers=self.token,
                                                         data={
                                                             "down": 80,
                                                             "heartbeat": 80,
                                                         })


        assert response_pressure.status_code == 200
        assert response_pressure_2.status_code == 200
        assert response_pressure_empty_optional.status_code == 422
        assert response_pressure_empty_upper.status_code == 422


    def test_get_list_pressure(self):
        response = self.client.get("/api/v1/pressure", headers=self.token)

        assert response.status_code == 200
        response_list = response.json()
        assert len(response_list["pressure"]) >= 2
        TestPressure.id_one_row = response_list["pressure"][0]["id"]


    def test_get_one_pressure(self):
        response = self.client.get(f"/api/v1/pressure/{TestPressure.id_one_row}", headers=self.token)

        assert response.status_code == 200

        response_one = response.json()
        assert bool(response_one["pressure"]) == True


    def test_update_pressure(self, pressue_updated_data):
        response = self.client.put(f"/api/v1/pressure/{TestPressure.id_one_row}",
                                   data=json.dumps(pressue_updated_data),
                                   headers=self.token)
        assert response.status_code == 200


        response_item = self.client.get(f"/api/v1/pressure/{TestPressure.id_one_row}", headers=self.token)
        assert response_item.status_code == 200
        response_one = response_item.json()
        pressue_updated_data['id'] = TestPressure.id_one_row
        assert response_one["pressure"]['upper'] == pressue_updated_data['upper']
        assert response_one["pressure"]['down'] == pressue_updated_data['down']
        assert response_one["pressure"]['heartbeat'] == pressue_updated_data['heartbeat']


    def test_delete_pressure(self):
        response = self.client.delete(f"/api/v1/pressure/{TestPressure.id_one_row}", headers=self.token)
        assert response.status_code == 200

        response_item = self.client.get(f"/api/v1/pressure/{TestPressure.id_one_row}", headers=self.token)
        assert response.status_code == 200

        response_one = response_item.json()
        assert bool(response_one["pressure"]) == False