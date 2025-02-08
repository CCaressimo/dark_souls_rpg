"""Actions for the game"""

import random
from ..entities.monsters import MONSTER_LIST
from ..entities.bosses import BOSS_LIST
from ..character.character import get_player_stats, get_strongest_skill, character_info, player_status

def random_combat(player_name, player_stats, temp_stats):
    """Random combat encounter with a monster"""

    encounter_chance = random.randint(1, 15)
    if encounter_chance == 1:
        enemy = random.choice(BOSS_LIST)
        print(f"You just walked into {enemy['name']}'s lair!\n")
    else:
        enemy = random.choice(MONSTER_LIST)
        print(f"You have encountered a {enemy['name']}!\n")

    skills = get_player_stats(player_stats)

    while True: # TODO add strength multiplier 2x damage, dex 2 hit (different damage), mage reduce enemy attack value
        # Check enemy death
        if int(enemy['health']) <= 0:
            print(f"You defeated the {enemy['name']}!")
            print(f"{player_name} gained {enemy['souls']} souls!\n")
            player_stats['souls'] += enemy['souls']
            break
        # Check player death
        if int(temp_stats['health']) <= 0:
            print(f"{player_name} has died!\n")
            break

        player_status(player_stats, temp_stats)
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
                print(f"{player_name} has {temp_stats['health']} health left!\n")

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

    player_status(player_stats, temp_stats)

    print(f"{player_name} came across a bonfire,\n")
    while True:
        response = input("(r)Rest and have a Siegbräu?\n"
                         "(s)Check your stats?\n"
                         "(l)Level up?\n"
                         "(i)Update inventory?\n"
                         "(q)Head back out into the world\n")
        if response == "r":
            # Update temp_stats and heal the player
            get_player_stats(player_stats)
            temp_stats['health'] = player_stats['health']  # Restore health to full
            temp_stats['attunement'] = player_stats['attunement']  # Restore attunement to full
            temp_stats['estus'] = player_stats['estus']  # Restore estus to full
            print(f"{player_name} has been replenished HP, MP and Estus Flasks!")
        elif response == "l":
            level_up( player_stats)
        elif response == "s":
            character_info(player_name, player_stats)
        elif response == "i":
            print(f"{player_name} updated their inventory")
        elif response == "q":
            print(f"{player_name} left the bonfire")
            break
    

def level_up(player_stats):
    """Level up the player"""

    x = player_stats['level']

    if player_stats['level'] > 15:
        soul_amount = 0.02 * x ** 3 + 3.06 * x ** 2 + 105.6 * x - 895
    else:
        soul_amount = x * 75

    level_up_choice = input(f"Choose a stat to increase:\n"
                     f"Souls needed: {abs(int(soul_amount))}\n"
                     f"Current Souls: {player_stats['souls']}\n"
                     f"(h) Health\n"
                     f"(a) Attunement\n"
                     f"(s) Strength\n"
                     f"(d) Dexterity\n"
                     f"(i) Intelligence\n"
                     f"(f) Faith\n"
                     f"(l) Luck\n")
    if player_stats['souls'] < int(soul_amount):
        print("Not enough souls to level up")
    else:
        if level_up_choice == "h":
            player_stats['health'] += 1
            player_stats['level'] += 1
            player_stats['souls'] -= int(soul_amount)
        elif level_up_choice == "a":
            player_stats['attunement'] += 1
            player_stats['level'] += 1
            player_stats['souls'] -= int(soul_amount)
        elif level_up_choice == "s":
            player_stats['strength'] += 1
            player_stats['level'] += 1
            player_stats['souls'] -= int(soul_amount)
        elif level_up_choice == "d":
            player_stats['dexterity'] += 1
            player_stats['level'] += 1
            player_stats['souls'] -= int(soul_amount)
        elif level_up_choice == "i":
            player_stats['intelligence'] += 1
            player_stats['level'] += 1
            player_stats['souls'] -= int(soul_amount)
        elif level_up_choice == "f":
            player_stats['faith'] += 1
            player_stats['level'] += 1
            player_stats['souls'] -= int(soul_amount)
        elif level_up_choice == "l":
            player_stats['luck'] += 1
            player_stats['level'] += 1
            player_stats['souls'] -= int(soul_amount)
