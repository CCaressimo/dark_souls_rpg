"""Actions for the game"""

import random
from ..entities.monsters import MONSTER_LIST
from ..entities.bosses import BOSS_LIST
from ..character.character import get_player_stats, get_strongest_skill, character_info

def random_combat(player_name, player_stats, temp_stats):
    """Random combat encounter with a monster"""

    encounter_chance = random.randint(1, 15)
    if encounter_chance == 1:
        enemy = random.choice(BOSS_LIST)
        print(f"You just walked into {enemy['name']}'s lair!")
    else:
        enemy = random.choice(MONSTER_LIST)
        print(f"You have encountered a {enemy['name']}!")

    skills = get_player_stats(player_stats)

    while True: # TODO add strength multiplier 2x damage, dex 2 hit (different damage), mage reduce enemy attack value
        # Check enemy death
        if int(enemy['health']) <= 0:
            print(f"You defeated the {enemy['name']}!")
            break
        # Check player death
        if int(temp_stats['health']) <= 0:
            print(f"{player_name} has died!")
            break

        character_info(player_name, player_stats, temp_stats)
        action = input("What do you want to do?\n(a) Attack\n(h) Heal\n(r) Run\n")
        player_roll = random.randint(1, 20)
        enemy_roll = random.randint(1, 20)

        if action == "a":
            print(f"\n{player_name} is attacking the {enemy['name']}!\n")
            strong_skill = get_strongest_skill(skills)
            if strong_skill == "strength":
                player_damage = int(skills[strong_skill] / 2)
                enemy_attack = int(enemy['attack'] / .5)
            elif strong_skill == "dexterity":
                enemy_attack = int(enemy['attack'] / 1)
                # First attack
                first_damage = int(skills[strong_skill] / 4)
                first_roll = random.randint(1, 20)
                if first_roll >= 10:  # Hit threshold
                    print(f"First strike hits! ({first_roll})")
                    player_damage = first_damage
                else:
                    print(f"First strike misses! ({first_roll})")
                    player_damage = 0

                # Second attack
                second_damage = int(skills[strong_skill] / 3)  # Slightly weaker second hit
                second_roll = random.randint(1, 20)
                if second_roll >= 12:  # Slightly harder to hit with second strike
                    print(f"Second strike hits! ({second_roll})")
                    player_damage += second_damage
                else:
                    print(f"Second strike misses! ({second_roll})")

                print(f"Total damage dealt: {player_damage}")
            elif strong_skill == "intelligence":
                player_damage = int(skills[strong_skill] / 4)
                enemy_attack = int(enemy['attack'] / 1.5)
            elif strong_skill == "faith":
                player_damage = int(skills[strong_skill] / 4)
                enemy_attack = int(enemy['attack'] / 1.5)
            print(f"{player_name} rolled a: {player_roll} + {player_damage}")
            player_attack = player_roll + player_damage

            print(f"You attacked the {enemy['name']} with a {player_attack}!")

            if player_roll == 20:
                print(f"{player_name} critically hits {enemy['name']} for {player_damage * 2} damage!")
                enemy["health"] -= player_damage * 2
            elif player_attack < enemy_attack:
                print(f"Ouch you took damage from a {enemy['name']}!\n")
                temp_stats['health'] -= enemy['damage']
                print(f"{player_name} has {player_stats['health']} health left!\n")

                print(f"{enemy['name']} has {enemy['health']} health left!\n")
            else:
                print(f"{enemy['name']} took {player_damage} damage!")
                enemy["health"] -= player_damage
                print(f"{enemy['name']} has {enemy['health']} health left!\n")

        elif action == "h":
            print(f"\n{player_name} is healing!\n")
            print(f"{player_name} rolled a: {player_roll} + {skills['intelligence']}\n")
            if (player_roll) == 20 and player_roll > enemy_roll:
                print(f"{player_name} successfully casts Bountiful Sunlight!\n")
                temp_stats['health'] += 5
            elif (player_roll + int(skills['intelligence'])) > 20 and player_roll > enemy_roll:
                print(f"{player_name} successfully casts Soothing Sunlight!\n")
                temp_stats['health'] += 3
            elif (player_roll + int(skills['intelligence'])) > 15 and player_roll > enemy_roll:
                print(f"{player_name} successfully casts Great Heal!\n")
                temp_stats['health'] += 1
            elif (player_roll + int(skills['intelligence'])) > 18 and player_roll > enemy_roll:
                print(f"{player_name} successfully casts Heal!\n")
                temp_stats['health'] += 2
            else:
                if enemy_roll > player_roll:
                    temp_stats['health'] -= enemy['damage']
                    print(f"{player_name} failed to heal {enemy['name']} successfully hit {enemy['damage']} damage!\n")
                else:
                    print(f"{player_name} failed to heal {enemy['name']} missed!\n")

        elif action == "r":
            print(f"\n{player_name} is attempt to run away!\n")
            player_dodge = player_roll + int(skills['dexterity'])
            print(f"{player_name} rolled a: {player_roll} + {skills['dexterity']}")
            if player_roll > enemy['attack']:
                print(f"{player_name} successfully ran away!\n")
                break
            else:
                if enemy_roll > player_dodge:
                    temp_stats['health'] -= enemy['damage']
                    print(f"{player_name} failed to run away and get hit {enemy['damage']}!\n")
                else:
                    print(f"{player_name} failed to run away but dodged the attack!\n")

        else:
            print(f"{player_name} killed the {enemy['name']}!\n")




def heal(player_name, player_stats, temp_stats):
    """Allows the character a chance to heal"""
    player_roll = random.randint(1, 20)
    print(player_roll)
    skills = get_player_stats(player_stats)

    if (player_roll + int(skills['intelligence'])) > 20:
        print(f"{player_name} uses a healing spell!\n")
        temp_stats['health'] += 2
    else:
        print("Not enough to heal...")

def rest_at_bonfire(player_name, player_stats, temp_stats):
    """Player can rest to gain health and flasks back"""
    character_info(player_name, player_stats, temp_stats)
    response = input(f"{player_name} came across a bonfire,\nrest and have a Siegbräu? (y/n)\n")
    if response == "y":
        # Level up section
        level_up = input(f"{player_name} leveled up! Choose a stat to increase:\n(h) Health\n(s) Strength\n(d) Dexterity\n(i) Intelligence\n(f) Faith\n")
        while True:
            if level_up == "h":
                player_stats['health'] += 1
                break
            elif level_up == "s":
                player_stats['strength'] += 1
                break
            elif level_up == "d":
                player_stats['dexterity'] += 1
                break
            elif level_up == "i":
                player_stats['intelligence'] += 1
                break
            elif level_up == "f":
                player_stats['faith'] += 1
                break
            else:
                print("Invalid stat")
                level_up = input(f"{player_name} leveled up! Choose a stat to increase:\n(h) Health\n(s) Strength\n(d) Dexterity\n(i) Intelligence\n(f) Faith\n")

        # Update temp_stats and heal the player
        get_player_stats(player_stats)
        temp_stats['health'] = player_stats['health']  # Restore health to full
        print(f"{player_name} has been healed!")
        character_info(player_name, player_stats, temp_stats)
    else:
        print(f"{player_name} left the bonfire")
