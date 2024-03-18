import requests


def get_users():
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    print(response.json())
    return response.json()