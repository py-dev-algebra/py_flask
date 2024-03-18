import requests


def get_users():
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    return response.json()