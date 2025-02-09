"""
Combat scenarios
"""

from ..character.character import player_status
from .actions import (
    rolls, cast_heal, drink_estus, generate_enemy_encounter,
    player_death, strength_attack, dexterity_attack
)

def random_combat(player_name, player_stats, temp_stats):
    """Random combat encounter with a monster"""

    enemy = generate_enemy_encounter()
    player_roll, enemy_roll, skills = rolls(player_stats)
    while True:

        # Check enemy death
        if int(enemy['health']) <= 0:
            print(f"You defeated the {enemy['name']}!")
            print(f"{player_name} gained {enemy['souls']} souls!\n")
            player_stats['souls'] += enemy['souls']
            break
        # Check player death
        if int(temp_stats['health']) <= 0:
            player_death(player_name, player_stats, temp_stats)
            break

        player_status(player_stats, temp_stats)
        action = input("What do you want to do?\n"
                       "(1) Attack\n"
                       "(2) Cast Heal\n"
                       "(3) Drink Estus\n"
                       "(4) Run\n")

        if action == "1":
            print(f"{player_name} is attacking!")
            attack = input("What do you want to do?\n"
                        "(1) Strength Attack\n"
                        "(2) Dexterity Attack\n")

            if attack == "1":
                strength_attack(player_name, player_stats, temp_stats, enemy)
            elif attack == "2":
                dexterity_attack(player_name, player_stats, temp_stats, enemy)
        elif action == "2":
            cast_heal(player_name, player_stats, temp_stats, enemy)
        elif action == "3":
            drink_estus(player_name, player_stats, temp_stats, enemy)
        elif action == "4":
            print(f"\n{player_name} is attempt to run away!\n")
            player_dodge = player_roll + (int(skills['dexterity']) / 4)
            print(f"{player_name} rolled a: "
                  f"{player_roll} + " + f"{round(int(skills['dexterity']) / 4)}")
            print(f"{enemy['name']} rolled: {enemy_roll}")
            if player_roll > enemy_roll:
                print(f"{player_name} successfully ran away!\n")
            else:
                if enemy_roll > player_dodge:
                    temp_stats['health'] -= enemy['damage']
                    print(f"{player_name} failed to run away and get hit {enemy['damage']}!\n")
                else:
                    print(f"{player_name} failed to run away but rolled away from "
                          f"{enemy['name']}'s attack!\n")
