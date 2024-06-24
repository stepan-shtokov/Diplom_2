import pytest
import requests
from helper_methods.helpers import PersonData
from static_data.urls import URL, Endpoints


@pytest.fixture
def create_user():  # Создание пользователя
    payload = PersonData.create_correct_user_data()
    response = requests.post(URL.main_url + Endpoints.CREATE_USER, data=payload)
    yield payload, response
    token = response.json()['accessToken']
    requests.delete(URL.main_url + Endpoints.DELETE_USER, headers={"Authorization": token})
