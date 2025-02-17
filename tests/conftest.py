import pytest
from api.api_courier import *

# Создание API метода
@pytest.fixture
def register():
    register = register_new_courier_and_return_login_password()
    yield register
    CourierAPI.delete_courier(register[0], register[1])
