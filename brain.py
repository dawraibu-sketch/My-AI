import random
from unknown import unknown
from greetings import get_greeting, get_wellbeing_response, get_farewell

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

    else:
        return random.choice(unknown)
