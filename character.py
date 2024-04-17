class Character:
    def __init__(self, name, strength, health):
        self.__name = name  # private attribute
        self.__strength = strength  # private attribute
        self.health = health

    def attack(self):
        return self.__strength * 3

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.__name}, Health: {self.health}, Strength: {self.__strength}"

class Hero(Character):  # Inheriting from Character
    def __init__(self, name, strength, health, heroism_level):
        super().__init__(name, strength, health)  # Call to the superclass constructor
        self.__heroism_level = heroism_level  # New private attribute specific to Hero

    def attack(self):
        # Overriding the attack method to include heroism level in the attack calculation
        base_attack = super().attack()
        return base_attack + self.__heroism_level * 2

    def inspire_ally(self):
        # New method specific to the Hero subclass
        if self.__heroism_level > 10:
            return "Inspires allies greatly increasing their morale!"
        else:
            return "Provides a modest boost to ally morale."

    def __str__(self):
        # Overriding the __str__ method to include heroism level
        basic_description = super().__str__()
        return f"{basic_description}, Heroism Level: {self.__heroism_level}"

# Example usage
if __name__ == "__main__":
    generic_character = Character("Gandalf", 30, 100)
    hero = Hero("Arthas", 40, 120, 15)
    print(generic_character)
    print(hero)
    print(hero.attack())
    print(hero.inspire_ally())


# Explanation:
# 1. Inheritance:
## The Hero class is derived from the Character class, inheriting attributes and methods such as __name, __strength, health, and attack().

# 2. Private Attributes:
## The Hero class introduces a new private attribute, __heroism_level, demonstrating how subclasses can extend the state and functionality of base classes.

# 3. Method Overriding and Polymorphism:
## The attack() method in the Hero class overrides the same method in the Character class, enhancing the attack strength based on the heroism level.
## The __str__() method is also overridden to include details about the heroism level in addition to the basic character description.

# 4. New Method:
## inspire_ally() is a method specific to the Hero class, showcasing additional capabilities and behaviors that might be expected from a hero character.