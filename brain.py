import random
from unknown import unknown
from greetings import get_greeting
def reply(message):
    message = message.lower()

    if message == "hello":
        return get_greeting()

    elif message == "how are you":
        return random.choice(wellbeing_responses)

    elif message == "what is your name":
        return "I am My-AI."

    elif message == "bye":
        return "Goodbye!"

    else:
        return random.choice(unknown)
