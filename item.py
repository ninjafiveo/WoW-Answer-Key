class Item:
    def __init__(self, name, item_type, power_boost):
        self.name = name
        self.item_type = item_type
        self.power_boost = power_boost

    def __str__(self):
        return f"Item: {self.name}, Type: {self.item_type}, Power Boost: {self.power_boost}"
