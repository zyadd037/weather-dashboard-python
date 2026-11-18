from unittest.mock import patch, Mock
import requests

from weather import get_weather


# Test 1: Successful API request
def test_get_weather_success():

    virtual_response = Mock()

    virtual_response.status_code = 200

    virtual_response.json.return_value = {
        "location": {
            "name": "London",
            "country": "United Kingdom"
        },
        "current": {
            "temp_c": 15,
            "humidity": 70,
            "wind_kph": 12,
            "condition": {
                "text": "Sunny"
            }
        }
    }

    with patch("weather.requests.get", return_value=virtual_response):

        result = get_weather("London")

    assert result["location"]["name"] == "London"
    assert result["current"]["temp_c"] == 15


# Test 2: Invalid city
def test_get_weather_invalid_city():

    virtual_response = Mock()

    virtual_response.status_code = 400

    virtual_response.json.return_value = {
        "error": {
            "code": 1006,
            "message": "No location found matching parameter"
        }
    }

    with patch("weather.requests.get", return_value=virtual_response):

        result = get_weather("WrongCity")

    assert result is None


# Test 3: Request Timeout
def test_get_weather_timeout():

    with patch(
        "weather.requests.get",
        side_effect=requests.exceptions.Timeout
    ):

        result = get_weather("London")

    assert result is None
