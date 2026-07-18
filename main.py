from brain import reply
from utils import get_greeting, get_date, get_time

creator = "Ibrahim"
memory = {}

print("Welcome to My-AI!")
print(get_greeting() + "!")
print('Type "bye" to exit.')

while True:
    user = input("You: ")

    if user.lower() == "bye":
        print("AI: Goodbye!")
        break

    if user.lower().startswith("my name is "):
        name = user[11:]
        memory["name"] = name
        print("AI: Nice to meet you,", name)
        continue

    if user.lower() == "what is my name":
        if "name" in memory:
            print("AI: Your name is", memory["name"])
        else:
            print("AI: I don't know your name yet.")
        continue

    if user.lower().startswith("i like "):
        thing = user[7:]
        memory["like"] = thing
        print("AI: I'll remember that.")
        continue

    if user.lower() == "what do i like":
        if "like" in memory:
            print("AI: You like", memory["like"])
        else:
            print("AI: I don't know what you like yet.")
        continue

    if user.lower() == "what time is it":
        print("AI: The time is", get_time())
    continue

    if user.lower() == "what is today's date":
        print("AI: Today is", get_date())
    continue

    if user.lower() == "who made you":
        print("AI: I was made by",creator)
    continue

    if user.lower() == "thank you":
        print("AI: You`re welcome")
    continue

    print("AI:", reply(user))

