def classify_intent(message):
    message = message.lower().strip()

    if message in ["hello", "hi", "hey"]:
        return "greeting"

    elif message in ["how are you", "how are you doing"]:
        return "wellbeing"

    elif message.startswith("calculate"):
        return "calculation"

    elif any(operator in message for operator in ["+", "*", "/", "plus", "minus", "times", "divided by"]):
        return "calculation"

    elif any(phrase in message for phrase in ["tell me a joke","make me laugh","give me a joke","say something funny"]):
        return "joke"

    elif any(phrase in message for phrase in ["tell me a quote","give me a quote","share a quote","inspire me","give me some inspiration"]):
        return "quote"

    elif any(phrase in message for phrase in ["tell me a fact","give me a fact","share a fact","give me some trivia","tell me something interesting"]):
        return "fact"

    elif "weather" in message or "temperature" in message:
        return "weather"

    elif message in ["bye", "goodbye", "see you"]:
        return "farewell"

    else:
        return "unknown"

