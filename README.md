# Дипломный проект. Задание 2: API Stellar Burgers

## Автотесты для сервиса 'Stellar Burgers'

## Файлы:
- allure_results - директория отчета о тестировании
- tests/test_create_order.py - проверки на создание заказа
- tests/test_create_user.py - проверки на создание пользователя
- tests/test_get_orders.py - проверки на получение заказов
- tests/test_login.py - проверки логина пользователя
- tests/test_update_user.py - проверки изменения данных пользователя
- helper_methods/helpers.py - методы генерации данных для регистрации
- static_data/ingredients.py -  данные об ингредиентах
- static_data/status_code.py - список статус-кодов ответа сервера
- static_data/text_response.py - список текстов ответа сервера
- static_data/urls - эндпоинты и url-адрес сервиса SB
- requirements.txt - файл с зависимостями
- conftest.py - фикстура создания\удаления юзера

Перед началом работы с репозиторием требуется установить зависимости: 
```
pip install -r requirements.txt
```
Запустить тесты:
```
pytest tests --alluredir=allure_results
```
Просмотреть отчет о тестировании:
```
allure serve allure_results
```
