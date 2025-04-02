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
    Flashcard("Reshiram", "644", "Dragon/Fire", "reshiram_image.jpg"),
    Flashcard("Zekrom", "644", "Dragon/Electric", "zekrom_image.jpg"),
    Flashcard("Charizard", "006", "Fire/Flying", "charizard_image.jpg"),
    Flashcard("Venusaur", "003", "Grass/Poison", "venusaur_image.jpg")
]



