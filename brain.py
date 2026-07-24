import random
from unknown import unknown
def reply(message):
    message = message.lower()

    if message == "hello":
        return "Hello! Nice to meet you."

    elif message == "what is your name":
        return "I am My-AI."

    elif message == "bye":
        return "Goodbye!"

    else:
        return random.choice(unknown)
