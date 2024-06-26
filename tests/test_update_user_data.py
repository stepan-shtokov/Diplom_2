import pytest
import requests
import allure

from static_data.urls import URL, Endpoints
from static_data.response_text import TextResponse
from static_data.status_codes import StatusCode
from helper_methods.helpers import PersonData


class TestChangeUserData:

    @allure.title('Change data after auth test')
    @allure.description('''
    1. Request to create a user;
    2. Request to change user data;
    3. Verify an answer;
    4. Delete user.
    ''')
    @pytest.mark.parametrize('data', [
        PersonData.create_correct_user_data()['name'],
        PersonData.create_correct_user_data()['email'],
        PersonData.create_correct_user_data()['password']
    ])
    def test_change_user_data(self, create_user, data):
        token = create_user[1].json()['accessToken']
        headers = {'Authorization': token}
        response = requests.patch(URL.main_url + Endpoints.CHANGE_DATA, headers=headers, data=data)
        assert response.status_code == StatusCode.OK
        assert response.json().get('success') is True

    @allure.title('Change data without auth test')
    @allure.description('''
    1. Request to change user data;
    2. Verify an answer.
    ''')
    @pytest.mark.parametrize('data', [
        PersonData.create_correct_user_data()['name'],
        PersonData.create_correct_user_data()['email'],
        PersonData.create_correct_user_data()['password']
    ])
    def test_change_unauthorized_user_data(self, data):
        response = requests.patch(URL.main_url + Endpoints.CHANGE_DATA, data=data)
        assert response.status_code == StatusCode.UNAUTHORIZED
        assert response.json().get('message') == TextResponse.UNAUTHORIZED_RESPONSE
