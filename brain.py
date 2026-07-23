import random
def reply(message):
    message = message.lower()

    if message == "hello":
        return "Hello! Nice to meet you."

    elif message == "what is your name":
        return "I am My-AI."

    elif message == "bye":
        return "Goodbye!"

    else:
        return ""AI:", random.choice(unknown)"
