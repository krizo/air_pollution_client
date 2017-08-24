import pytest
from aqicn_api_client.client import AqicnApiClient, ApiException

STATION_METRICS = [
    "co", "h", "no2", "p", "pm10", "pm25", "t"
]
CITY_METRICS = [
    "h", "no2", "p", "pm10", "t"
]
MAIN_METRICS = [
    "co", "h", "no2", "p", "pm10", "pm25", "t"
]
api_client = AqicnApiClient()

def test_station_stats():
    station_stats = api_client.station_stats("krasińskiego")
    _check_metrics(station_stats)

def test_city_stats():
    city_stats = api_client.city_stats("kraków")
    _check_metrics(city_stats)

def test_station_measure():
    for measure in STATION_METRICS:
        assert api_client.station_measure("krasińskiego", measure) != None

def test_city_measure():
    for measure in CITY_METRICS:
        assert api_client.city_measure("kraków", measure) != None


def _check_metrics(station_stats):
    for metric, value in station_stats.items():
        assert metric in MAIN_METRICS
        assert value['v'] != None
