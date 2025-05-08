import json

class Flashcard:
    def __init__(self, make, dex, type):
        self.make = make
        self.dex = dex
        self.type = type

newMake = input("Input a Pokemon. \n")
newDex = input("Input the Pokemon dex number. \n")
newType = input("Input the Pokemon type. If multiple, separate with a dash. \n")
newPokemon = Flashcard(newMake, newDex, newType)

# Load existing data
try:
    with open("FlashCards.json", "r") as file:
        pokemon_data = json.load(file)
except FileNotFoundError:
    pokemon_data = []

# Append new poke
pokemon_data.append(newPokemon.__dict__)

# Save to a JSON file
with open("FlashCards.json", "w") as file:
    json.dump(pokemon_data, file, indent = 4)

# Student Mode

score = 0
streak = 0

# Load existing data
try:
    with open("FlashCards.json", "r") as file:
        pokemon_data = json.load(file)
except FileNotFoundError:
    pokemon_data = []

for pokemon in pokemon_data:
    ansType = input(f"\nWhat is the type of {pokemon['make']}? \n")
    if ansType == pokemon['type']:
        score += 1
        streak += 1
        print("Good job. ")
        if streak >= 3:
            bonusPoints = streak - 2
            score += bonusPoints
            print(f"Bonus points acquired. You have a streak of {streak} correct answers. You get {bonusPoints}. ")

    else:
        streak = 0
        print(f"No stupir idior try again next time. ")

    ansDex = input(f"\nWhat is the dex number of {pokemon['make']}? \n")
    if ansDex == pokemon['dex']:
        score += 1
        streak += 1
        print("Good job. ")
        if streak >= 3:
            bonusPoints = streak - 2
            score += bonusPoints
            print(f"Bonus points acquired. You have a streak of {streak} correct answers. You get {bonusPoints}. ")

    else:
        streak = 0
        print(f"No stupir idior try again next time. ")