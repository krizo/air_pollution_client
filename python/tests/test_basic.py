import pytest
from aqicn_api_client.client import AqicnApiClient, ApiException
import os

api_client = AqicnApiClient()
STATION_ATTRIBUTES = {
    "aqi": [],
    "idx": [],
    "attributions": [ "url", "name" ],
    "city": [ "geo", "name", "url"],
    "dominentpol": [],
    "iaqi": [ "h", "p", "t", "pm10" ],
    "time": [ "s", "tz", "v"]
}

def test_token_taken_from_environ():
    assert api_client.token == os.environ['AQICN_TOKEN']

def test_client_with_invalid_token():
    invalid_token = 'foo'
    invalid_client = AqicnApiClient(token=invalid_token)
    with pytest.raises(ApiException) as exception:
        res = invalid_client.get_city("shanghai")
    assert exception.value.msg == "Invalid key"

def test_existing_city_response_status():
    res = api_client.get_city("shanghai")
    assert any(res)

def test_not_existing_city_response_status():
    with pytest.raises(ApiException) as exception:
        res_bad = api_client.get_city("foo")
    assert exception.value.msg == 'Unknown station'

def test_search_existing_keyword():
    krakow_stations = api_client.search("kraków")
    assert len(krakow_stations) == 4

def test_nearest_station():
    nearest_station = api_client.neartest_station()
    assert nearest_station.keys() == STATION_ATTRIBUTES.keys()
