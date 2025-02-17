import requests
import random
import string
import allure
import pytest
from api.api_courier import *


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

@allure.step("Сначала создаем курьера")
def register_new_courier_and_return_login_password():
    login_pass = []
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)


    if response.status_code == 201:
        login_pass.extend([login, password, first_name])

    return login_pass

@allure.step("Сначала создаем курьера, чтобы потом его удалить из базы")
@pytest.fixture
def create_and_delete_courier():
    # Создаем курьера и получаем его данные
    courier_data = register_new_courier_and_return_login_password()
    yield courier_data  # Передаем данные в тест

    # Логинимся, чтобы получить id курьера
    login_response = CourierAPI.login_courier(courier_data[0], courier_data[1])
    courier_id = login_response.json()["id"]

    # Удаляем курьера после завершения теста
    login, password, _ = courier_data
    CourierAPI.delete_courier(courier_id)