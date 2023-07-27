import allure
from src.utils import api


link = 'starships/?search=falcon'


@allure.feature("API")
def test_get_falcon_starship_by_api():
    api_request = api.search_for_falcon_starship(link)
    api.get_all_pilots_of_falcon(api_request)
