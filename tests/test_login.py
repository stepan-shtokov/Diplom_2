import allure
import requests

from helper_methods.helpers import PersonData
from static_data.urls import URL, Endpoints
from static_data.status_codes import StatusCode


class TestLoginUser:
    @allure.title('Test logging with existing user')
    @allure.description('''
    1. Request to create a user;
    2. Request to login the user;
    3. Verify an answer;
    4. Delete user.
    ''')
    def test_user_login(self, create_user):
        response = create_user
        login = requests.post(URL.main_url + Endpoints.LOGIN, data=response[0])
        assert login.status_code == StatusCode.OK
        assert login.json().get("success") is True

    @allure.title('Test logging with none-data user')
    @allure.description('''
    1. Request to login user without registration;
    2. Verify an answer.
    ''')
    def test_login_nonexistent_user(self):
        login_request = requests.post(URL.main_url + Endpoints.LOGIN,
                                      data=PersonData.create_incorrect_user_data_without_name())
        assert login_request.status_code == StatusCode.UNAUTHORIZED
        assert login_request.json().get("success") is False
