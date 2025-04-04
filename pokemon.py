import json

class Flashcard:
    def __init__(self, make, dex, type, image=None):
        self.make = make
        self.dex = dex
        self.type = type
        self.image = image

    def display_info(self):
        return f"{self.dex} {self.type} {self.model}"
    
    def to_dict(self):
        return {"make": self.make, "dex": self.dex, "type": self.type, "image": self.image}
    
pokemon = [
    Flashcard("Reshiram", "643", "Dragon/Fire", "reshiram.jpg"),
    Flashcard("Zekrom", "644", "Dragon/Electric", "zekrom.jpg"),
]

# Convert objects to dictionaries
pokemon_data = [Flashcard.to_dict() for Flashcard in pokemon]

# Save to a JSON file
with open("FlashCards.json", "w") as file:
    json.dump(pokemon_data, file, indent = 4)

new_pokemon = Flashcard("Chevrolet", "Malibu", 2024, "malibu_image.jpg")

# Load existing data
try:
    with open("FlashCards.json", "r") as file:
        pokemon_data = json.load(file)
except FileNotFoundError:
    pokemon_data = []

# Append new poke
pokemon_data.append(new_pokemon.to_dict())

# Save updated data back to file
with open("cars.json", "w") as file:
    json.dump(pokemon_data, file, indent=4)