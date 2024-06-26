import requests
import allure

from static_data.urls import URL, Endpoints
from static_data.status_codes import StatusCode
from static_data.response_text import TextResponse
from static_data.ingredients_hash_data import Ingredients


class TestGetOrder:
    @allure.title('Get order by authorized user')
    @allure.description('''
    1. Request to create user;
    2. Request to create order by authorized user;
    3. Request to get user's orders;
    4. Verify an answer;
    5. Delete user.
    ''')
    def test_get_orders_by_authorized_user(self, create_user):
        token = create_user[1].json()['accessToken']
        headers = {'Authorization': token}
        response_create_order = requests.post(URL.main_url + Endpoints.CREATE_ORDER,
                                              headers=headers, data=Ingredients.correct_ingredients_hash_data)
        response_get_order = requests.get(URL.main_url + Endpoints.GET_ORDERS, headers=headers)
        assert response_get_order.status_code == StatusCode.OK
        assert response_create_order.json()['order']['number'] == response_get_order.json()['orders'][0]['number']

    @allure.title('Get order by unauthorized user')
    @allure.description('''
    1. Request to get user's orders;
    2. Verify an answer.
    ''')
    def test_get_orders_by_unauthorized_user(self):
        response_get_orders = requests.get(URL.main_url + Endpoints.GET_ORDERS)
        assert response_get_orders.status_code == StatusCode.UNAUTHORIZED
        assert TextResponse.UNAUTHORIZED_RESPONSE in response_get_orders.text
