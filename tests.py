import requests
from constants import BASE_URL


def test_endpoint(endpoint_name: str):
    response = requests.get(BASE_URL.format(endpoint_name=endpoint_name))
    return response.json()
