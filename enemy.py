from character import Character

class Enemy(Character):  # Inheriting from Character
    def __init__(self, name, strength, health, hostility_level):
        super().__init__(name, strength, health)
        self.hostility_level = hostility_level  # New attribute specific to Enemy

    def attack(self):
        # Overriding the attack method with additional hostility factor
        return super().attack() + self.hostility_level

    def __str__(self):
        original_description = super().__str__()
        return f"{original_description}, Hostility Level: {self.hostility_level}"
