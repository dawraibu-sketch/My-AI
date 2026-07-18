from brain import reply

memory = {}

print("Welcome to My-AI!")
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

    print("AI:", reply(user))
