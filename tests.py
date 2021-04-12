import requests
from constants import BASE_URL


def test_get_endpoint(endpoint_name: str):
    response = requests.get(BASE_URL.format(endpoint_name=endpoint_name))
    return response.json()


def test_post_endpoint(endpoint_name: str):
    response = requests.post(BASE_URL.format(endpoint_name=endpoint_name))
    return response


def test_put_endpoint(endpoint_name: str):
    response = requests.put(BASE_URL.format(endpoint_name=endpoint_name))
    return response.json()


def test_delete_endpoint(endpoint_name: str):
    response = requests.delete(BASE_URL.format(endpoint_name=endpoint_name))
    return response.json()
