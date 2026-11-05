import requests


def get_location():
    try:
        response = requests.get(
            "https://ipwho.is/",
            timeout=10
        )

        response.raise_for_status()
        data = response.json()

        if data.get("success"):
            return {
                "city": data["city"],
                "country": data["country"],
                "latitude": data["latitude"],
                "longitude": data["longitude"],
                "timezone": data["timezone"]["id"]
            }

        return None

    except (requests.RequestException, ValueError, KeyError, TypeError):
        return None

