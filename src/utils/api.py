import allure
import requests
import logging
from src.models.model import ResponseModel

baseUrl = 'https://swapi.dev/api/'


def __send_request(url):
    if 'http' in url:
        response = requests.get(url)
    else:
        response = requests.get(baseUrl + url)
    return ResponseModel(status=response.status_code, body=response.json())


def search_for_falcon_starship(falcon_search_url):
    with allure.step("Searching for Falcon starship"):
        logging.info('Searching for Falcon starship...')
        response = __send_request(falcon_search_url)
        assert response.status == 200, "The API request has failed!"
        assert 'Falcon' in response.body['results'][0]['name'], "The Falcon starship is not found"
        logging.info('Falcon has been found!\n')
        return response


def get_all_pilots_of_falcon(response):
    with allure.step("Searching for Falcon crew"):
        logging.info('Searching for Falcon crew...')
        logging.info('The crew that was driving Falcon ever:')
        for i in response.body['results'][0]['pilots']:
            pilot_name = __send_request(i).body['name']
            logging.info(pilot_name)
