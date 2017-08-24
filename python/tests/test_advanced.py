import pytest
from aqicn_api_client.client import AqicnApiClient, ApiException
import os

STATION_ATTRIBUTES = {
    "aqi": [],
    "idx": [],
    "attributions": [ "url", "name" ],
    "city": [ "geo", "name", "url"],
    "dominentpol": [],
    "iaqi": [ "h", "p", "t", "pm10" ],
    "time": [ "s", "tz", "v"]
}

api_client = AqicnApiClient()

def test_nearest_station():
    nearest_station = api_client.neartest_station()
    for attribute, params in STATION_ATTRIBUTES.items():
        if any(params):
            if isinstance(nearest_station[attribute], list):
                actual_keys = set(sum([list(key.keys()) for key in nearest_station[attribute] ], []))
            else:
                actual_keys = set(nearest_station[attribute])
            assert actual_keys == set(params)
