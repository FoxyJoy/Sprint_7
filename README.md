# Тема "API тестирование" курс ЯндексПрактикум | Sprint_7
Тема "Тестирование API" курс ЯндексПрактикум | Sprint_7
Для тестирования был выбран сервис [«Яндекс.Самокат»](https://qa-scooter.praktikum-services.ru/) 
В связи с грядущим релизом были созданы проверки: 


---
### О репозитиории
#### В директории [utils](utils) лежат требуемая для тестов [рандомная регистрация курьера](utils/courier_utils.py).

#### В директории [api](pages) лежат actions [для "Тестирования курьера"](api/api_courier.py), [для "Создания заказа"](api/api_order.py)



### [Логин курьера](tests/tests_login.py) 
- Проверка, что курьер может авторизоваться
```
def test_login_courier_true(self)
```

- Проверка, что для авторизации нужно передать все обязательные поля
```
def test_login_courier_missing_fild(self)
```

- Проверка, что система возвращает ошибку, если неправильно указать логин
```
test_login_courier_invalid_credentials(self)
```

- Проверка, система возвращает ошибку, если неправильно указать пароль
```
def test_password_courier_invalid_credentials(self)
```


 ### [Создание курьера](tests/tests_methods_courier.py)
- Проверка курьер создается
```
def test_create_courier_true(self)
```

- Проверка, что если создать пользователя с логином, который уже есть, возвращается ошибка
```
 def test_create_duplicate_courier(self)
```

- Проверка, на пропуск обязательного поле при создании курьера
```
def test_create_courier_missing_field(self)
```

### [Удалить курьера](tests/tests_delete_courier.py)
- Удалить курьера
```
def test_create_courier_true(self)
```
- Удалить курьера с невалидным id
```
def test_delete_courier_without_id(self)
```

 ### [Создание заказа](tests/tests_methods_order.py)
- При создании заказа можно указать цвет — BLACK
```
def test_create_order_with_black_color(self)
```

- При создании заказа можно указать серый цвет
```
 def test_create_order_with_grey_color(self)
```

- При создании заказа можно указать два цвета
```
def test_create_order_with_two_color(self)
```

- При создании заказа можно не указывать цвет
```
def test_create_order_without_color(self)
```
- Тело ответа содержит track
```
def test_get_orders_track(self)
```

### Тестовый Фреймворк 
- pytest / selenium / allure
---

Перед работой с репозиторием требуется установить зависимости 
``` shell
pip3 install -r requirements.txt
```
Запустить все тесты из директории tests
```shell
pytest tests --alluredir=allure_results
```
Посмотреть отчет в веб версии пройденного прогона
``` shell
allure serve allure_results
```