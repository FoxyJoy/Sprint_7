import pytest
import requests
import allure
from utils.courier_utils import *
from api.api_courier import CourierAPI

class TestDeleteCourier:
    @allure.title('Удалить курьера')
    def test_create_courier_true(self):
        # Сначала создаем курьера, чтобы потом его удалить
        courier_data = register_new_courier_and_return_login_password()

        # Логинимся, чтобы получить id курьера
        login_response = CourierAPI.login_courier(courier_data[0], courier_data[1])
        courier_id = login_response.json()["id"]

        # Удаляем курьера
        response = CourierAPI.delete_courier(courier_id)
        assert response.status_code == 200
        assert response.json() == {"ok": True}

    @allure.title('Удалить курьера с невалидным id')
    def test_delete_courier_without_id(self):
        invalid_id = "1234567890"
        # Сначала создаем курьера, чтобы потом его удалить
        courier_data = register_new_courier_and_return_login_password()

        # Логинимся, чтобы получить id курьера
        login_response = CourierAPI.login_courier(courier_data[0], courier_data[1])
        courier_id = login_response.json()["id"]

        # Удаляем курьера
        response = CourierAPI.delete_courier(invalid_id)
        assert response.status_code == 404
        assert "Курьера с таким id нет" in response.text

