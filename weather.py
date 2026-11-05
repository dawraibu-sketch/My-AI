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

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        current = data.get("current")

        if current is None or "temperature_2m" not in current:
            return None

        return {
            "city": location["city"],
            "temperature": current["temperature_2m"]
        }

    except (requests.RequestException, ValueError, KeyError, TypeError):
        return None
        
