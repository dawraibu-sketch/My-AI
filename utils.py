from datetime import datetime
from zoneinfo import ZoneInfo

def get_greeting():
    hour = datetime.now().hour

    if hour < 12:
        return "Good morning"

    elif hour < 18:
        return "Good afternoon"

    else:
        return "Good evening"


def get_time():
    return datetime.now().strftime("%I:%M %p")


def get_date():
    return datetime.now().strftime("%d %B %Y")
