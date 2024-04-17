class Environment:
    def __init__(self, name, description):
        self.__name = name  # private attribute
        self.__description = description  # private attribute

    def get_details(self):
        return f"Environment: {self.__name}, Description: {self.__description}"

    def __str__(self):
        return self.get_details()

class EnchantedForest(Environment):
    def __init__(self, name, description, magic_level):
        super().__init__(name, description)  # Initialize attributes from the base class
        self.magic_level = magic_level  # New attribute specific to EnchantedForest

    def get_details(self):
        # Overriding the get_details method to include magic_level
        basic_details = super().get_details()
        return f"{basic_details}, Magic Level: {self.magic_level}"

    def __str__(self):
        return self.get_details()

# Example of how the use of super() and polymorphism works in practice
if __name__ == "__main__":
    basic_env = Environment("Generic Plains", "A vast open field that is windy and cold.")
    enchanted_forest = EnchantedForest("Mystic Woods", "A mysterious and ancient forest that echoes with magic.", 10)

    print(basic_env)  # Outputs: Environment: Generic Plains, Description: A vast open field that is windy and cold.
    print(enchanted_forest)  # Outputs: Environment: Mystic Woods, Description: A mysterious and ancient forest that echoes with magic., Magic Level: 10


# Explanation:
# 1. Private Attributes: In the Environment class, both __name and __description are private attributes, emphasizing the principle of encapsulation. They are meant to prevent direct access from outside the class, ensuring that the internal representation of the environment is hidden from external manipulation.

# 2. Inheritance: The EnchantedForest class is a subclass of Environment. This setup demonstrates inheritance by extending the generic environment to something more specific with additional characteristics, in this case, a magical level.

# 3. Super() Usage: The use of super().__init__(name, description) in the EnchantedForest constructor ensures that the Environment class's constructor is called, allowing the EnchantedForest class to initialize the inherited attributes properly.

# 4. Polymorphism and Method Overriding: By overriding the get_details() and __str__() methods in the EnchantedForest, this subclass modifies the behavior of these methods to include additional information (i.e., magic_level). This is a clear example of polymorphism where the subclass provides specific behavior that extends and enhances the functionality provided by the superclass.