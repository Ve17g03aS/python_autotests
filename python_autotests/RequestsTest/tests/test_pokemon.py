import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '25708a6593e13ca352fbc729277919cb'
HEADERS = {'Content-Type' : 'application/json', "trainer_token" : TOKEN}

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {"trainer_id": 2206})
    assert response.status_code == 200

def test_trainers_name():
    response = requests.get(url = f'{URL}/trainers', params = {"trainer_id": 2206})
    assert response.json()['data'][0]['trainer_name'] == 'Lars'