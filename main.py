from brain import reply
from utils import get_greeting, get_date, get_time
from calculator import Calculator
from jokes import jokes
from quotes import quotes
from facts import facts
from coinflip import flip_coin
from rps import play_rps
from riddles import play_riddle
from help import show_help
from memory import load_memory, save_memory
from knowledge import load_knowledge, save_knowledge
from teach import teach_fact, recall_fact
import time
import random

creator = "Ibrahim"
memory = load_memory()
knowledge = load_knowledge()

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
        save_memory(memory)
        print("AI: Nice to meet you,", name)
        continue

    if user.lower() == "what is my name":
        if "name" in memory:
            print("AI: Your name is", memory["name"])
        else:
            print("AI: I don't know your name yet.")
        continue

    if user.lower().startswith("i like "):
        like = user[7:] 
        if "likes" not in memory:
            memory["likes"] = []     
        if like not in memory["likes"]:
            memory["likes"].append(like)
            save_memory(memory)
            print("AI: I'll remember that.")
        else:
            print("AI: You already told me that.")
        continue

    if user.lower() == "what do i like":
        if "likes" in memory:
            print("AI: You like:")
            for item in memory["likes"]:
                print("-", item)
        else:
            print("AI: I don't know what you like yet.")
        continue

    if user.lower().startswith("forget that i like "):
        like = user[19:]
        if "likes" in memory and like in memory["likes"]:
            memory["likes"].remove(like)
            save_memory(memory)
            print("AI: Okay, I'll forget that you like", like)
        else:
            print("AI: I don't remember that.")
        continue

    if user.lower().startswith("i don't like "):
        dislike = user[13:]
        if "dislikes" not in memory:
            memory["dislikes"] = []
        if dislike not in memory["dislikes"]:
            memory["dislikes"].append(dislike)
            save_memory(memory)
            print("AI: I'll remember that.")
        else:
            print("AI: You already told me that.")
        continue

    if user.lower() == "what don't i like":
        if "dislikes" in memory:
            print("AI: You don't like:")
            for item in memory["dislikes"]:
                print("-", item)
        else:
            print("AI: I don't know what you don't like yet.")
        continue

    if user.lower().startswith("forget that i don't like "):
        dislike = user[25:]
        if "dislikes" in memory and dislike in memory["dislikes"]:
            memory["dislikes"].remove(dislike)
            save_memory(memory)
            print("AI: Okay, I'll forget that you don't like", dislike)
        else:
            print("AI: I don't remember that.")
        continue

    if user.lower().startswith("my favorite food is "):
        food = user[20:]
        if "favorite_foods" not in memory:
            memory["favorite_foods"] = []
        if food not in memory["favorite_foods"]:
            memory["favorite_foods"].append(food)
            save_memory(memory)
            print("AI: I'll remember that.")
        else:
            print("AI: You already told me that.")
        continue

    if user.lower() == "what are my favorite foods":
        if "favorite_foods" in memory:
            print("AI: Your favorite foods are:")
            for food in memory["favorite_foods"]:
                print("-", food)
        else:
            print("AI: I don't know your favorite foods yet.")
        continue

    if user.lower().startswith("forget that my favorite food is "):
        food = user[32:]
        if "favorite_foods" in memory and food in memory["favorite_foods"]:
            memory["favorite_foods"].remove(food)
            save_memory(memory)
            print("AI: Okay, I'll forget that your favorite food is ", food)
        else:
            print("AI: I don't remember that.")
        continue

    if user.lower().startswith("my favorite game is "):
        game = user[20:]
        if "favorite_games" not in memory:
            memory["favorite_games"] = []
        if game not in memory["favorite_games"]:
            memory["favorite_games"].append(game)
            save_memory(memory)
            print("AI: I'll remember that.")
        else:
            print("AI: You already told me that.")
        continue

    if user.lower() == "what are my favorite games":
        if "favorite_games" in memory:
            print("AI: Your favorite games are:")
            for game in memory["favorite_games"]:
                print("-", game)
        else:
            print("AI: I don't know your favorite games yet.")
        continue

    if user.lower().startswith("forget that my favorite game is "):
        game = user[32:]
        if "favorite_games" in memory and game in memory["favorite_games"]:
            memory["favorite_games"].remove(game)
            save_memory(memory)
            print("AI: Okay, I'll forget that your favorite game is ", game)
        else:
            print("AI: I don't remember that.")
        continue
    
    if user.lower().startswith("i live in "):
        country = user[10:]
        memory["country"] = country
        save_memory(memory)
        print("AI: I'll remember that.")
        continue

    if user.lower() == "where do i live":
        if "country" in memory:
            print("AI: You live in ", memory["country"])
        else:
            print("AI: I don't know where you live yet.")
        continue

    if user.lower().startswith("my birthday is "):
        birthday = user[15:]
        memory["birthday"] = birthday
        save_memory(memory)
        print("AI: I'll remember that.")
        continue

    if user.lower() == "when is my birthday":
        if "birthday" in memory:
            print("AI: Your BirthDay is on ", memory["birthday"])
        else:
            print("AI: I don't know when your birthday is yet.")
        continue

    if user.lower().startswith("my favorite colour is "):
        colour = user[22:]
        memory["colour"] = colour
        save_memory(memory)
        print("AI: I'll remember that.")
        continue

    if user.lower() == "what is my favorite colour":
        if "colour" in memory:
            print("AI: Your favorite colour is ", memory["colour"])
        else:
            print("AI: I don't know what your favorite colour is yet.")
        continue

    if user.lower() in ["forget everything", "reset memory", "clear memory"]:
        memory.clear()
        save_memory(memory)
        print("AI: All saved memories have been erased.")
        continue

    if user.lower() == "what do you know about me":
        print("")
        print("AI: Here's what I know about you:")
        if "name" in memory:
            print("• Your name is", memory["name"])
        if "age" in memory:
            print("• You are", memory["age"], "years old")
        if "country" in memory:
            print("• You live in", memory["country"])
        if "favorite_color" in memory:
            print("• Your favorite color is", memory["favorite_color"])
        if "likes" in memory:
            print("• You like:")
            for item in memory["likes"]:
                print("  -", item)
        if "dislikes" in memory:
            print("• You don't like:")
            for item in memory["dislikes"]:
                print("  -", item)
        if "favorite_foods" in memory:
            print("• Your favorite foods are:")
            for food in memory["favorite_foods"]:
                print("  -", food)
        if "favorite_games" in memory:
            print("• Your favorite games are:")
            for game in memory["favorite_games"]:
                print("  -", game)
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

    if user.lower() in ["help", "commands", "what can you do", "what do you do", "what are your commands"]:
        show_help()
        continue

    if user.lower().startswith("teach:"):
        sentence = user[6:].strip()
        teach_fact(knowledge, sentence)
        continue

    if user.lower().startswith("what is "):
        recall_fact(knowledge, user)
        continue

    print("AI:", reply(user))
