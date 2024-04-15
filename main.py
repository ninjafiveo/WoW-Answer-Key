# Import classes from team members
from character import Character
from enemy import Enemy
from item import Item
from environment import Environment

def main():
    hero = Character("Arthas", 30, 100)
    villain = Enemy("Mal'Ganis", 25, 80, 5)
    sword = Item("Excalibur", "Sword", 20)
    forest = Environment("Elwynn Forest", "A vast and idyllic forest.")

    # Example of interactions
    print(hero)
    print(villain)
    villain.take_damage(hero.attack())
    print("After attack:")
    print(villain)
    print(sword)
    print(forest)

if __name__ == "__main__":
    main()
