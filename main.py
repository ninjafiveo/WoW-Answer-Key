# Import classes from team members
from character import Character, Hero
from enemy import Enemy
from item import Item, Weapon
from environment import Environment

def main():
    print("Welcome to the Mini Text Adventure!")
    hero_name = input("Enter your hero's name: ")
    hero = Hero(hero_name, 40, 120, 15)
    sword = Weapon("Excalibur", "Sword", 20)
    forest = Environment("Enchanted Forest", "A forest that is alive with magic and mystery.")

    print("\nYour journey begins...")
    print(f"You are {hero}, armed with {sword}.")
    print(f"You enter the {forest}.")

    enemy = Enemy("Dark Sorcerer", 35, 100, 8)
    print(f"\nA wild {enemy} appears!\n")

    while enemy.health > 0 and hero.is_alive():
        choice = input("Do you want to 'attack' or 'inspire'? ").lower()
        if choice == "attack":
            damage = hero.attack()
            print(f"You attack the {enemy} dealing {damage} damage!")
            enemy.take_damage(damage)
        elif choice == "inspire":
            inspiration = hero.inspire_ally()
            print(f"You attempt to inspire your imaginary allies. {inspiration}")
        else:
            print("Invalid choice. The battle continues!")

        # Enemy retaliates
        if enemy.is_alive():
            enemy_damage = enemy.attack()
            print(f"The {enemy} fights back, dealing {enemy_damage} damage!")
            hero.take_damage(enemy_damage)
        else:
            print(f"\nYou have defeated the {enemy}!")

        if not hero.is_alive():
            print("You have fallen in battle... Game Over.")
            break

    if hero.is_alive():
        print("\nCongratulations! You have survived the Enchanted Forest.")

if __name__ == "__main__":
    main()
