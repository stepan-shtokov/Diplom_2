import requests
import allure

from static_data.urls import URL, Endpoints
from static_data.status_codes import StatusCode
from static_data.response_text import TextResponse
from static_data.ingredients_hash_data import Ingredients


class TestCreateOrder:

    @allure.title('Order by authorized user test')
    @allure.description('''
    1. Request to create user;
    2. Request to create order with authorized user;
    3. Verify an answer;
    4. Delete user.
    ''')
    def test_create_order_with_authorized_user(self, create_user):
        token = create_user[1].json()['accessToken']
        headers = {'Authorization': token}
        response = requests.post(URL.main_url + Endpoints.CREATE_ORDER, headers=headers, data=Ingredients.correct_ingredients_hash_data)
        assert response.status_code == StatusCode.OK
        assert response.json().get('success') is True

    @allure.title('Order by unauthorized user test')
    @allure.description('''
    1. Request to create order without authorization;
    2. Verify an answer.
    ''')
    def test_create_order_by_unauthorized_user(self):
        response = requests.post(URL.main_url + Endpoints.CREATE_ORDER, data=Ingredients.correct_ingredients_hash_data)
        assert response.status_code == StatusCode.OK
        assert response.json().get('success') is True

    @allure.title('Test order by authorized user without valid hash data')
    @allure.description('''
    1. Request to create user;
    2. Request to create order with non-valid ingredients hash from authorized user;
    3. Verify an answer;
    4. Delete user.
    ''')
    def test_create_order_with_invalid_hash(self, create_user):
        token = create_user[1].json()['accessToken']
        headers = {'Authorization': token}
        response = requests.post(URL.main_url + Endpoints.CREATE_ORDER,
                                 headers=headers, data=Ingredients.incorrect_ingredients_hash_data)
        assert response.status_code == StatusCode.INTERNAL_SERVER_ERROR
        assert TextResponse.INTERNAL_SERVER_ERROR in response.text

    @allure.title('Test order by authorized user without ingredients test')
    @allure.description('''
    1. Request to create user;
    2. Request to create order without ingredients by authorized user;
    3. Verify an answer;
    4. Delete user.
    ''')
    def test_create_order_with_none_ingredients(self, create_user):
        token = create_user[1].json()['accessToken']
        headers = {'Authorization': token}
        response = requests.post(URL.main_url + Endpoints.CREATE_ORDER,
                                 headers=headers, data=Ingredients.empty_ingredients_data)
        assert response.status_code == StatusCode.BAD_REQUEST
        assert response.json().get('success') is False
