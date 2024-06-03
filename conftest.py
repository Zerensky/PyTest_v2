# Фикстуры 

import pytest
import requests
import yaml

@pytest.fixture(scope='session')
def config():
    with open('config.yaml', 'r') as file:
        return yaml.safe_load(file)

@pytest.fixture(scope='session')
def auth_token(config):
    login_url = f"{config['site_url']}/gateway/login"
    response = requests.post(login_url, data={
        "username": config['username'],
        "password": config['password']
    })
    response.raise_for_status()
    return response.json()['token']
