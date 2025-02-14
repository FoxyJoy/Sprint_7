import pytest
import requests
import allure
from api.api_courier import *
from utils.courier_utils import register_new_courier_and_return_login_password

class TestLogin:
    @allure.title('Курьер может авторизоваться')
    def test_login_courier_true(self):
        courier_data = register_new_courier_and_return_login_password()
        response = CourierAPI.login_courier(courier_data[0], courier_data[1])
        assert response.status_code == 200
        assert "id" in response.json()

        # assert len(courier_data) == 3, "Courier registration failed"

    @allure.title('Для авторизации нужно передать все обязательные поля')
    def test_login_courier_missing_fild(self):
        response = CourierAPI.login_courier("login_only", "")
        assert response.status_code == 400
        assert "Недостаточно данных для входа" in response.text

    @allure.title('Система возвращает ошибку, если неправильно указать логин')
    def test_login_courier_invalid_credentials(self):
        response = CourierAPI.login_courier("invalid_login", "valid_password")
        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.text

    @allure.title('Система возвращает ошибку, если неправильно указать пароль')
    def test_password_courier_invalid_credentials(self):
        response = CourierAPI.login_courier("invalid_login", "valid_password")
        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.text
