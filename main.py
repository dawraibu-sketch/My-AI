from brain import reply

print("Welcome to My-AI!")
print("Type 'bye' to exit.")

while True:
    user = input("You: ")

    answer = reply(user)

    print("AI:", answer)

    if user.lower() == "bye":
        break
