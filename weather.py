from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_KEY = os.getenv("API_KEY")


def get_weather(city):

    url = "https://api.weatherapi.com/v1/current.json"

    params = {
        "key": API_KEY,
        "q": city,
        "aqi": "no"
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        data = response.json()

        if response.status_code != 200:
            error_message = data.get("error", {}).get(
                "message", "Unknown API error"
            )
            print("API Error:", error_message)
            return None

        return data

    except requests.exceptions.Timeout:
        print("Error: Request has timed out!")

    except requests.exceptions.ConnectionError:
        print("Error: Check your internet connection!")

    except requests.exceptions.RequestException:
        print("Error: Something went wrong with request!")

    except (KeyError, TypeError, ValueError):
        print("Error: Invalid API response!")

    return None

    





