from character import Character

class Enemy(Character):  # Inheriting from Character
    def __init__(self, name, strength, health, hostility_level):
        super().__init__(name, strength, health)  # Initialize inherited attributes using super()
        self.__hostility_level = hostility_level  # Private attribute specific to Enemy
        self.__intelligence = 5  # Default intelligence for all enemies, private attribute

    def plan_attack(self):
        # Private method that decides the type of attack based on hostility and intelligence
        if self.__intelligence > 10:
            return "uses a strategic attack!"
        elif self.__hostility_level > 7:
            return "uses a berserk attack!"
        else:
            return "uses a standard attack!"

    def attack(self):
        # Overriding the attack method with additional behavior based on hostility level
        attack_type = self.plan_attack()
        return f"{self.__str__()} {attack_type}"

    def __str__(self):
        # Overriding the __str__ method to include hostility_level
        basic_description = super().__str__()  # Call to the parent class's __str__ method
        return f"{basic_description}, Hostility Level: {self.__hostility_level}, Intelligence: {self.__intelligence}"

# Example usage
if __name__ == "__main__":
    generic_enemy = Enemy("Goblin", 15, 100, 8)
    print(generic_enemy.attack())  # Demonstrates polymorphism and method overriding


# Explanation
# 1. Private Attributes:

## __hostility_level: A private attribute that modifies attack behaviors.
## __intelligence: Another private attribute used to determine the type of attack strategy an enemy uses.
# 2. Inheritance:
## The Enemy class inherits from Character, using super() to initialize inherited attributes.

# 3. Method Overriding and Polymorphism:

## attack(): This method is overridden to incorporate an enemy-specific attack type, which uses the private method plan_attack() to determine how the enemy attacks based on its intelligence and hostility.
## plan_attack(): A new method introduced to determine the type of attack based on the enemy's hostility level and intelligence. This method is not accessible from outside the class, showcasing encapsulation within polymorphism.
## __str__(): Overridden to add more descriptive text about the enemy, including its hostility level and intelligence, demonstrating how subclasses can enhance and extend the functionality of methods from the superclass.