import random
import time

def flip_coin():
    print("AI: Flipping the coin...")
    time.sleep(1)

    print("🪙")
    time.sleep(1)

    print("AI:", random.choice(["Heads!", "Tails!"]))
