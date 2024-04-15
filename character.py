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
