import requests
import allure

class OrderAPI:
    main_url = "https://qa-scooter.praktikum-services.ru/api/v1/orders"


    @staticmethod
    @allure.step("Создание заказа")
    def create_order(first_name, last_name, address, metro_station, phone, rent_time, delivery_date, comment,
                     color=None):
        payload = {
            "firstName": first_name,
            "lastName": last_name,
            "address": address,
            "metroStation": metro_station,
            "phone": phone,
            "rentTime": rent_time,
            "deliveryDate": delivery_date,
            "comment": comment,
            "color": color # Опционально
        }
        return requests.post(OrderAPI.main_url, json=payload)


    @staticmethod
    @allure.step("Получение трек-номера заказа")
    def get_order_by_track(track):
        return requests.get(f"{OrderAPI.main_url}/track", params={"t": track})
