import requests
import allure

class CourierAPI:
    main_url = "https://qa-scooter.praktikum-services.ru/api/v1/courier"

    @staticmethod
    @allure.step("Создание курьера")
    def create_courier(login, password, first_name):
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        return requests.post(CourierAPI.main_url, data=payload)

    @staticmethod
    @allure.step("Логинимся")
    def login_courier(login, password):
        payload = {
            "login": login,
            "password": password
        }
        return requests.post(f"{CourierAPI.main_url}/login", data=payload)

    @staticmethod
    @allure.step("Удаление курьера")
    def delete_courier(courier_id):
        return requests.delete(f"{CourierAPI.main_url}/{courier_id}")
