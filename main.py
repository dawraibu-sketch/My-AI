from brain import reply
from utils import get_greeting, get_date, get_time
from calculator import Calculator
from jokes import jokes
from quotes import quotes
from facts import facts
from coinflip import flip_coin
from rps import play_rps
from riddles import play_riddle
import time
import random

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
        Calculator()
        print("Back to the AI!")
        continue

    if user.lower() == "tell me a joke":
        print("AI:", random.choice(jokes))
        continue

    if user.lower() == "tell me a quote":
        print("AI:", random.choice(quotes))
        continue

    if user.lower() == "tell me a fact":
        print("AI:", random.choice(facts))
        continue

    if user.lower() in ["flip a coin", "coin flip", "flip coin"]:
        flip_coin()
        continue

    if user.lower() in ["dice roll", "roll dice", "roll a dice"]:
        print("Rolling the dice...")
        time.sleep(1)
        print("🎲")
        time.sleep(1)
        print(f"You rolled a {random.randint(1, 6)}!")
        continue

    if user.lower() in ["rps", "rock paper scissors"]:
        play_rps()
        continue

    if user.lower() in ["riddle", "riddles", "ask me a riddle", "tell me a riddle", "give me a riddle"]:
        print("")
        print("Thinking...")
        time.sleep(1.25)
        print("")
        play_riddle()
        continue

    print("AI:", reply(user))
