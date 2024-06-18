import random

def roll_dice():
    return random.randint(1, 6)

# Simulate rolling the dice
print("Rolling the dice...")
result = roll_dice()
print(f"The dice shows: {result}")
