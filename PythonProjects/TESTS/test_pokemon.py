import requests
import pytest

def test_status_code():
    response = requests.get('https://pokemonbattle.me:5000/trainers')
    assert response.status_code == 200

def test_string_in_body():
    response = requests.get ('https://pokemonbattle.me:5000/trainers', params={'trainer_id': 'id_тренера'})
    assert response.json()['trainer_name'] == 'id_тренера'
