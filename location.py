import requests


def get_location():
    response = requests.get("https://ipwho.is/")
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
