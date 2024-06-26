import pytest
import allure
import requests

from helper_methods.helpers import PersonData
from static_data.urls import URL, Endpoints
from static_data.status_codes import StatusCode
from static_data.response_text import TextResponse


class TestCreateUser:
    @allure.title('Unique user creation test')
    @allure.description('''
    1. Send request to create user;
    2. Verify an answer;
    3. Delete user.
    ''')
    def test_create_user(self, create_user):
        response = create_user
        assert response[1].json().get("success") is True
        assert response[1].status_code == StatusCode.OK

    @allure.title('Double user creation test')
    @allure.description('''
    1. Send request to create user;
    2. Get data for registration;
    3. Resend request to create user;
    4. Verify an answer;
    5. Delete user.
    ''')
    def test_double_create_user(self, create_user):
        response = create_user
        payload = response[0]
        response_double_register = requests.post(URL.main_url + Endpoints.CREATE_USER, data=payload)
        assert response_double_register.status_code == StatusCode.FORBIDDEN
        assert response_double_register.json().get('message') == TextResponse.DOUBLE_USER_CREATED

    @allure.title('Create user with incorrect data test')
    @allure.description(''''
    1. Send request to create user with incorrect data;
    2. Verify an answer.
    ''')
    @pytest.mark.parametrize('payload', [
        PersonData.create_incorrect_user_data_without_email(),
        PersonData.create_incorrect_user_data_without_password(),
        PersonData.create_incorrect_user_data_without_name()
    ])
    def test_incorrect_user_data_create(self, payload):
        response = requests.post(URL.main_url + Endpoints.CREATE_USER, data=payload)
        assert response.status_code == StatusCode.FORBIDDEN and response.json().get("success") is False
