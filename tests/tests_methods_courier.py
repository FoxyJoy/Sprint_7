import pytest
import allure
from api.api_courier import CourierAPI
from utils.courier_utils import register_new_courier_and_return_login_password

class TestCouriers:
    @allure.title('Cоздание курьера')
    def test_create_courier_true(self):
        courier_data = register_new_courier_and_return_login_password()
        assert len(courier_data) == 3

    @allure.title('Если создать пользователя с логином, который уже есть, возвращается ошибка')
    def test_create_duplicate_courier(self):
        courier_data = register_new_courier_and_return_login_password()
        response = CourierAPI.create_courier(courier_data[0], courier_data[1], courier_data[2])
        assert response.status_code == 409
        assert "Этот логин уже используется" in response.text

    @allure.title('Пропустили обязательное поле при создании курьера')
    def test_create_courier_missing_field(self):
        courier_data = register_new_courier_and_return_login_password()
        response = CourierAPI.create_courier("login_only", "", "")
        assert response.status_code == 400
        assert "Недостаточно данных для создания учетной записи" in response.text


