import random
from datetime import datetime
from zoneinfo import ZoneInfo


def get_timezone():
    try:
        local_timezone = datetime.now().astimezone().tzinfo

        if local_timezone is not None:
            return local_timezone

    except Exception:
        pass

    return ZoneInfo("UTC")


def get_greeting():
    timezone = get_timezone()
    hour = datetime.now(timezone).hour

    if hour < 12:
        return "Good morning"
    elif hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"


def get_time():
    timezone = get_timezone()
    current_time = datetime.now(timezone).strftime("%I:%M %p")

    responses = [
        f"The current time is {current_time}.",
        f"It's {current_time}.",
        f"Right now, it's {current_time}.",
        f"The time is {current_time}."
    ]

    return random.choice(responses)


def get_date():
    timezone = get_timezone()
    return datetime.now(timezone).strftime("%d %B %Y")

