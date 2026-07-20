from brain import reply
from utils import get_greeting, get_date, get_time
from calculator import add, subtract, multiply, divide, power, root, Menu

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
        print("AI: I was made by", creator)
        continue

    if user.lower() == "thank you":
        print("AI: You're welcome!")
        continue

    if user.lower() == "help" or user.lower() == "what can you do":
        print("AI: I can:\n- Greet you\n- Remember your name\n- Tell the time\n- Tell today's date\n- Tell who created me\n- Calculate")
        continue

    if user.lower() == "calculate":
        while True:
            Menu()
            choice = input("Enter choice (1/2/3/4/5/6): ")

            if choice in ('1', '2', '3', '4', '5', '6'):
                try:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))

                    if choice == '1':
                        print(num1, "+", num2, "=", add(num1, num2))

                    elif choice == '2':
                        print(num1, "-", num2, "=", subtract(num1, num2))

                    elif choice == '3':
                        print(num1, "*", num2, "=", multiply(num1, num2))

                    elif choice == '4':
                        if num2 == 0:
                            print("AI: You cannot divide by zero.")
                            continue
                        print(num1, "/", num2, "=", divide(num1, num2))

                    elif choice == '5':
                        print(num1, "**", num2, "=", power(num1, num2))

                    elif choice == '6':
                        if num2 == 0:
                            print("AI: The root number cannot be zero.")
                            continue
                        print(num1, "√", num2, "=", round(root(num1, num2), 2))

                except ValueError:
                    print("AI: Please enter a valid number.")
                    continue

                except ZeroDivisionError:
                    print("AI: You cannot divide by zero.")
                    continue

                next_calculation = input("Let's do another calculation? (yes/no): ")

                if next_calculation.lower() != "yes":
                    break

            else:
                print("AI: Invalid choice.")

        continue

    print("AI:", reply(user))
