class Item:
    def __init__(self, name, item_type):
        self.__name = name  # private attribute
        self.__item_type = item_type  # private attribute

    def use(self):
        return f"This {self.__item_type} has no special effects."

    def __str__(self):
        return f"Item: {self.__name}, Type: {self.__item_type}"

class Weapon(Item):  # Inheriting from Item
    def __init__(self, name, item_type, power_boost):
        super().__init__(name, item_type)  # Using super to initialize inherited attributes
        self.power_boost = power_boost  # Specific attribute to Weapon

    def use(self):
        # Overriding the use method to include power_boost functionality
        return f"Using {self.__name} grants a power boost of {self.power_boost}."

    def __str__(self):
        # Overriding the __str__ method to include power_boost
        basic_description = super().__str__()
        return f"{basic_description}, Power Boost: {self.power_boost}"

# Example of how the use of super() and polymorphism works in practice
if __name__ == "__main__":
    generic_item = Item("Healing Potion", "Potion")
    excalibur = Weapon("Excalibur", "Sword", 20)

    print(generic_item.use())  # Outputs: This Potion has no special effects.
    print(excalibur.use())  # Outputs: Using Excalibur grants a power boost of 20.
    print(excalibur)  # Outputs: Item: Excalibur, Type: Sword, Power Boost: 20

# Explanation:
# 1. Private Attributes: In Item, __name and __item_type are private attributes to demonstrate encapsulation. They cannot be accessed directly outside their class.

# 2. Inheritance: The Weapon class is a subclass of Item, inheriting its properties and methods. This demonstrates inheritance by extending Item to more specific types.

# 3. Super() Usage: super().__init__(name, item_type) in the Weapon class's constructor shows how to call the superclass's constructor, ensuring that the base class is correctly initialized before adding subclass-specific properties.

# 4. Polymorphism and Method Overriding: The use() and __str__() methods in the Weapon class override the same methods in Item. This is a demonstration of polymorphism where the subclass methods provide different behavior than the superclass method. For instance, the use() method in Weapon now includes functionality related to power_boost, which is specific to Weapon and not just any Item.