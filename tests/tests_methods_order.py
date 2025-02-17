import pytest
import requests
import allure
from api.api_order import OrderAPI

class TestColors:
    @allure.title('При создании заказа можно указать цвет(а) или не указывать цвет')
    @pytest.mark.parametrize("colors", [
        pytest.param(["BLACK"], id="BLACK color"),
        pytest.param(["GREY"], id="GREY color"),
        pytest.param(["BLACK", "GREY"], id="BLACK and GREY colors"),
        pytest.param([], id="No color")
    ])
    def test_create_order_with_colors(self, colors):
        response = OrderAPI.create_order(
            "John", "Karter", "Красная, 142", "1", "+78007778899", 5, "2025-02-14", "Aloha", colors
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