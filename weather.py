import requests
from location import get_location


def get_weather():
    location = get_location()

    if location is None:
        return None

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": location["latitude"],
        "longitude": location["longitude"],
        "current": "temperature_2m"
    }

    response = requests.get(url, params=params)
    data = response.json()

    return {
        "city": location["city"],
        "temperature": data["current"]["temperature_2m"]
    }
