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
    _check_attributes(nearest_station)

def test_station_stats():
    station_stats = api_client.station_stats("krasińskiego")
    _check_attributes(station_stats)


def _check_attributes(station):
        for attribute, params in STATION_ATTRIBUTES.items():
                actual_keys = None
                if any(params):
                    if isinstance(station[attribute], list):
                        actual_keys = set(sum([list(key.keys()) for key in station[attribute] ], []))
                    else:
                        actual_keys = set(station[attribute])
                    assert all(key in actual_keys for key in set(params))
