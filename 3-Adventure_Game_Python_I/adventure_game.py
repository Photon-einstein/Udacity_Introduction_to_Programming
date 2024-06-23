import time
import random


def print_pause(str):
    print(str)
    time.sleep(1)


def intro(enemy):
    enemies = ["Dragon", "Witch", "Vampire", "Snake"]
    enemy = random.choice(enemies)
    print_pause(
        f"A {enemy} as been terrifying a village.\n" +
        "you arrive at that village and decide to help the local people.\n" +
        "The problem is that you have just a small knife and some\n" +
        "peasantry clothes.")
    return enemy


def options(items, enemy):
    prompt = """
You can go to the Castle, to a farm or to a lake.
Witch one do you go ?
Press '1' to go to the Castle.
Press '2" to go to the farm
Press '3' to go to the lake.
"""
    destiny = numeric_input(prompt, 1, 3)
    if destiny == 1:
        outcome = visit_castle(items, enemy)
        if outcome == "True":
            return
    elif destiny == 2:
        visit_farm(items)
        options(items, enemy)
    elif destiny == 3:
        visit_lake(items)
        options(items, enemy)
    else:
        print_pause("Wrong input given, no such option is available")
        options(items, enemy)


def visit_castle(items, enemy):
    print_pause(f"You arrive at the castle and it appears a {enemy}\n" +
                "in front of you")
    if "Sword" in items and "Armor" in items:
        print_pause(
            "You unleash you sword and start the fight,\n " +
            f"the {enemy} tries to attack you but the armor resists.\n" +
            f"You are able to kill the {enemy}. The local people thank\n" +
            "you, you are a hero now, congratulations.")
        return False
    elif "Sword" in items:
        print_pause("You unleash you sword and start the fight,\n" +
                    f"the {enemy} tries to attack you but you are not able\n" +
                    "to defend and get killed. Game Over.")
        return get_input()
    else:
        print_pause("You unleash you small knife and start the fight, the \n" +
                    f"{enemy} attack you over and over so you get killed.\n" +
                    "Game Over.")
        return get_input()


def get_input():
    while True:
        prompt = """Would you like to play again ? 'y' for yes or
'n' for no."""
        reply = string_input(prompt, ['y', 'n'])
        if reply.lower() == 'y':
            start_game()
        elif reply.lower() == 'n':
            killed = True
            return killed
        else:
            print_pause("Wrong input given.")


def visit_farm(items):
    if "Sword" not in items:
        print_pause("In the farm you found a mighty sword, and you\n" +
                    "throw away the small knife.")
        items.append("Sword")
    else:
        print_pause("You already visited the farm, nothing more to do here.")


def visit_lake(items):
    if "Armor" not in items:
        print_pause("In the lake you found a imponent armor, so you\n" +
                    "dress it up and proceed.")
        items.append("Armor")
    else:
        print_pause("You already visited the lake, nothing more to do here.")


def string_input(prompt, options):
    while True:
        print_pause(prompt)
        option = input().lower()
        if option in options:
            return option
        print(f'Option {option} is invalid. Try again!')


def numeric_input(prompt, minimum, maximum):
    while True:
        print_pause(prompt)
        option = input()
        if option.isnumeric():
            option = int(option)
            if minimum <= option <= maximum:
                return option
            print(f'Option must be in the range [{minimum}, {maximum}].')
        else:
            print(f'Invalid input: {option} is not numeric.')


def start_game():
    enemy = ""
    items = []
    enemy = intro(enemy)
    options(items, enemy)


start_game()
