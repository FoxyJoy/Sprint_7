import pytest
import allure
from api.api_courier import CourierAPI
import requests
from api.api_courier import *
from utils.courier_utils import *

class TestCouriers:
    @allure.title('Cоздание курьера')
    def test_create_courier_true(self, create_and_delete_courier):
        courier_data = create_and_delete_courier

        # Проверяем, что данные курьера возвращаются в виде списка
        assert isinstance(courier_data, list)    #Данные курьера должны быть списком
        assert len(courier_data) == 3    #Список данных курьера должен содержать 3 элемента (логин, пароль, имя)

        # Логинимся, чтобы убедиться, что курьер создан
        login_response = CourierAPI.login_courier(courier_data[0], courier_data[1])
        assert login_response.status_code == 200    #Ожидался статус-код 200 при логине

        # Проверяем, что в ответе есть id курьера
        assert "id" in login_response.json()     #В ответе должен быть id курьера

    @allure.title('Если создать пользователя с логином, который уже есть, возвращается ошибка')
    def test_create_duplicate_courier(self, create_and_delete_courier):
        courier_data = create_and_delete_courier
        # Пытаемся создать курьера с теми же данными
        response = CourierAPI.create_courier(courier_data[0], courier_data[1], courier_data[2])
        assert response.status_code == 409
        assert "Этот логин уже используется" in response.text

    @allure.title('Пропустили обязательное поле при создании курьера')
    def test_create_courier_missing_field(self):
        # Пытаемся создать курьера без обязательных полей
        response = CourierAPI.create_courier("login_only", "", "")
        assert response.status_code == 400
        assert "Недостаточно данных для создания учетной записи" in response.text
