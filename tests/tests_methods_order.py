import pytest
import requests
import allure
from api.api_order import OrderAPI

class TestColors:
    @allure.title('При создании заказа можно указать цвет — BLACK')
    def test_create_order_with_black_color(self):
        response = OrderAPI.create_order(
                "John", "Karter", "Красная, 142", "1", "+78007778899", 5, "2025-02-14", "Aloha", ["BLACK"])
        assert response.status_code == 201
        assert "track" in response.json()

    @allure.title('При создании заказа можно указать серый цвет')
    def test_create_order_with_grey_color(self):
        response = OrderAPI.create_order(
                "John", "Karter", "Красная, 142", "1", "+78007778899", 5, "2025-02-14", "Aloha", ["GREY"])
        assert response.status_code == 201
        assert "track" in response.json()

    @allure.title('При создании заказа можно указать два цвета')
    def test_create_order_with_two_color(self):
        response = OrderAPI.create_order(
            "John", "Karter", "Красная, 142", "1", "+78007778899", 5, "2025-02-14", "Aloha", ["BLACK", "GREY"])
        assert response.status_code == 201
        assert "track" in response.json()

    @allure.title('При создании заказа можно не указывать цвет')
    def test_create_order_without_color(self):
        response = OrderAPI.create_order(
            "John", "Karter", "Красная, 142", "1", "+78007778899", 5, "2025-02-14", "Aloha"
        )
        assert response.status_code == 201
        assert "track" in response.json()


    @allure.title('Тело ответа содержит track')
    def test_get_orders_track(self):
        order_response = OrderAPI.create_order(
            "John", "Karter", "Красная, 142", "1", "+78007778899", 5, "2025-02-14", "Aloha"
        )
        track = order_response.json()["track"]
        response = OrderAPI.get_order_by_track(track)
        assert response.status_code == 200
        assert "order" in response.json()
