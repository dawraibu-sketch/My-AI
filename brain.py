import random
from unknown import unknown
from greetings import get_greeting, get_wellbeing_response, get_farewell
from weather import get_weather

def reply(message):
    message = message.lower()

    if message == "hello":
        return get_greeting()

    elif message == "how are you":
        return get_wellbeing_response()

    elif message == "what is your name":
        return "I am My-AI."

    elif message == "bye":
        return get_farewell()

    elif message in ["what is the weather", "what's the weather"]:
        weather = get_weather()
        if weather:
            return f"The current temperature in {weather['city']} is {weather['temperature']}°C."
        return "I couldn't get the weather right now."

    else:
        return random.choice(unknown)
