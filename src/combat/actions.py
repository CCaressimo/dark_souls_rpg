"""
Actions for the game
"""

import random
from ..entities.monsters import MONSTER_LIST
from ..entities.bosses import BOSS_LIST
from ..character.character import (
    get_player_stats,character_info, player_status
)

def rolls(player_stats):
    """Call for random rolls and skills"""
    player_roll = random.randint(1, 20)
    enemy_roll = random.randint(1, 20)
    skills = get_player_stats(player_stats)
    return player_roll, enemy_roll, skills

def generate_enemy_encounter():
    """Choose a random enemy encounter"""
    encounter_chance = random.randint(1, 15)
    if encounter_chance == 1:
        enemy = random.choice(BOSS_LIST)
        print(f"You just walked into {enemy['name']}'s lair!\n")
    else:
        enemy = random.choice(MONSTER_LIST)
        print(f"You have encountered a {enemy['name']}!\n")
    return enemy

def strength_attack(player_name, player_stats, temp_stats, enemy):
    """Player strength attack"""
    player_roll, enemy_roll, skills = rolls(player_stats)
    player_skill = int(skills['strength'] / 2)
    player_damage = random.randint(round(player_skill / 2), player_skill)
    enemy_attack = round(enemy['attack'] / 1.7)
    player_attack = player_roll + player_skill
    enemy_action = ['dodges', 'blocks', 'deflects']
    enemy_block = enemy_roll + enemy_attack

    print(f"\n{player_name} is charging a power attack!")
    print(f"{player_name} rolls a: {player_roll} + {player_skill}")
    print(f"{enemy['name']} rolls a: {enemy_roll} + {enemy_attack}\n")

    if player_roll == 20 or enemy_roll == 1:
        player_damage *= 3
        enemy['health'] -= player_damage
        print(f"{player_name} does a critical backstab on "
              f"{enemy['name']} for {player_damage} damage!")
        print(f"{enemy['name']} has {enemy['health']} health left!\n")

    elif player_attack > enemy_block:
        enemy['health'] -= player_damage
        print(f"{player_name} crushes {enemy['name']} with a {player_damage}!")
        print(f"{enemy['name']} has {enemy['health']} health left!\n")
    elif player_roll == 1 or enemy_roll == 20:
        temp_stats['health'] -= enemy['damage'] * 2
        print(f"{enemy['name']} does a critical counter on "
              f"{player_name} for {enemy['damage'] * 2} damage!")
        print(f"{player_name} has {temp_stats['health']} health left!\n")
    else:
        print(f"{enemy['name']} " + random.choice(enemy_action) + f" {player_name}'s attack!\n")

def dexterity_attack(player_name, player_stats, temp_stats, enemy):
    """Player dexterity attack"""
    skills = get_player_stats(player_stats)
    player_skill = int(skills['dexterity'] / 4)
    player_combo = random.randint(1, player_skill)
    enemy_attack = round(enemy['attack'] / 2)
    enemy_action = ['dodges', 'blocks', 'deflects']

    print(f"\n{player_name} is goes for a light combo attack!")
    if player_combo > 1:
        print(f"{player_name} is attacking with {player_combo} hits!")
    else:
        print(f"{player_name} is attacking with {player_combo} hit!")

    for i in range(player_combo):
        player_roll, enemy_roll, skills = rolls(player_stats)
        player_damage = random.randint(1, player_skill)
        player_attack = player_roll + player_skill
        enemy_block = enemy_roll + enemy_attack

        print(f"{player_name} rolls a: {player_roll} + {player_skill}")
        print(f"{enemy['name']} rolls a: {enemy_roll} + {enemy_attack}\n")
        if player_roll == 20 or enemy_roll == 1:
            player_damage *= 2
            enemy['health'] -= player_damage 
            print(f"{player_name} does a critical backstab on "
                  f"{enemy['name']} for {player_damage} damage!")
            print(f"{enemy['name']} has {enemy['health']} health left!\n")

        elif player_attack > enemy_block:
            enemy['health'] -= player_damage
            print(f"{player_name} strikes {enemy['name']} with a {player_damage}!")
            print(f"{enemy['name']} has {enemy['health']} health left!\n")
        elif player_roll == 1 or enemy_roll == 20:
            temp_stats['health'] -= enemy['damage'] * 2
            print(f"{enemy['name']} does a critical counter on "
                  f"{player_name} for {enemy['damage'] * 2} damage!")
            print(f"{player_name} has {temp_stats['health']} health left!\n")
        else:
            print(f"{enemy['name']} " + random.choice(enemy_action) + f" {player_name}'s attack!\n")


# def spell_attack(player_name, player_stats, temp_stats, enemy):
#     """Player intelligence attack"""
#     player_roll, enemy_roll, skills = rolls(player_stats)
#     player_skill = int(skills['intelligence'] / 4)
#     enemy_attack = round(enemy['attack'] / 2)
#     enemy_action = ['dodges', 'blocks', 'deflects']


# def enemy_attack(player_name, player_stats, temp_stats, enemy):
#     """Enemy attack"""
#     enemy_roll, enemy_attack, enemy_action = rolls(enemy)
#     enemy_damage = random.randint(round(enemy['attack'] / 2), enemy['attack'])
#     enemy_block = enemy_roll + enemy_attack

def cast_heal(player_name, player_stats, temp_stats, enemy):
    """Player action to cast a healing spell"""
    player_roll, enemy_roll, skills = rolls(player_stats)
    print(f"\n{player_name} is attempting to healing!")
    total_roll = player_roll + round(int(skills['intelligence']) / 4)
    print(f"{player_name} rolled a: {player_roll} + " + f"{round(int(skills['intelligence']) / 4)}")
    print(f"{enemy['name']} rolled: {enemy_roll}")

    # Define healing spells and requirements
    healing_spells = [
        {'name': 'Bountiful Sunlight', 'req': 20, 'heal': 5, 'mp': 4, 'crit_only': True},
        {'name': 'Soothing Sunlight', 'req': 20, 'heal': 3, 'mp': 3, 'crit_only': False},
        {'name': 'Great Heal', 'req': 18, 'heal': 2, 'mp': 2, 'crit_only': False},
        {'name': 'Heal', 'req': 15, 'heal': 1, 'mp': 1, 'crit_only': False}
    ]

    # Check if any spell can be cast
    for spell in sorted(healing_spells, key=lambda x: x['req'], reverse=True):
        check = player_roll if spell['crit_only'] else total_roll
        if check >= spell['req'] and player_roll > enemy_roll:
            print(f"{player_name}'s healing roll: {check}")
            if temp_stats['attunement'] >= spell['mp']:
                print(f"{player_name} successfully casts {spell['name']}!\n")
                if temp_stats['health'] + spell['heal'] > player_stats['health']:
                    temp_stats['health'] = player_stats['health']
                else:
                    temp_stats['health'] += spell['heal']
                temp_stats['attunement'] -= spell['mp']
                return
            print(f"{player_name} does not have enough mp to cast {spell['name']}!\n")

    if enemy_roll > total_roll:
        print(f"{player_name} failed to heal, "
              f"and {enemy['name']} punished "
              f"the player for {enemy['damage']} damage!\n")
        temp_stats['health'] -= enemy['damage']
    elif enemy_roll <= total_roll:
        print(f"{player_name} failed to heal, "
              f"but dodged {enemy['name']}'s attack!\n")


def drink_estus(player_name, player_stats, temp_stats, enemy):
    """Allows the character a chance to heal"""
    player_roll, enemy_roll, skills = rolls(player_stats)
    print(f"\n{player_name} attempts takes a sip of their Estus Flask!")
    print(f"{player_name} rolled a: {player_roll} + " + f"{round(int(skills['dexterity']) / 4)}")
    print(f"{enemy['name']} rolled: {enemy_roll}")
    total_roll = player_roll + (int(skills['dexterity']) / 4)
    estus_heal = player_stats['health'] * .25

    if total_roll >= enemy_roll:
        if temp_stats['estus'] > 0:
            temp_stats['estus'] -= 1
            if temp_stats['health'] + estus_heal > player_stats['health']:
                print(f"{player_name} drank to full health from their flask!\n")
                temp_stats['health'] = player_stats['health']
            else:
                print(f"{player_name} drank {round(estus_heal)} health from their flask!\n")
                temp_stats['health'] += round(estus_heal)
        else:
            print(f"{player_name} has no Estus Flasks left!")
    elif player_roll < enemy['damage']:
        print(f"{enemy['name']} punishes {player_name} for trying to heal!\n")
        temp_stats['health'] -= enemy['damage']
    else:
        print(f"{player_name} needed to dodge {enemy['name']}'s "
                f"attack and could not drink from their flask!\n")


def rest_at_bonfire(player_name, player_stats, temp_stats):
    """Player can rest to gain health and flasks back,
      level up, update inventory, or head back out into the world"""

    player_status(player_stats, temp_stats)
    print(f"{player_name} came across a bonfire,\n")
    while True:
        response = input("(1)Rest and have a Siegbräu?\n"
                         "(2)Check your stats?\n"
                         "(3)Level up?\n"
                         "(4)Update inventory?\n"
                         "(5)Head back out into the world\n")
        if response == "1":
            # Update temp_stats and heal the player
            get_player_stats(player_stats)
            temp_stats['health'] = player_stats['health']  # Restore health to full
            temp_stats['attunement'] = player_stats['attunement']  # Restore attunement to full
            temp_stats['estus'] = player_stats['estus']  # Restore estus to full
            print(f"{player_name} has been replenished HP, MP and Estus Flasks!")
        elif response == "2":
            character_info(player_name, player_stats)
        elif response == "3":
            level_up(player_name, player_stats)
        elif response == "4":
            print(f"{player_name} updated their inventory")
        elif response == "5":
            print(f"{player_name} left the bonfire")
            break


def level_up(player_name, player_stats):
    """Level up the player"""

    x = player_stats['level']
    if player_stats['level'] > 15:
        soul_amount = 0.02 * x ** 3 + 3.06 * x ** 2 + 105.6 * x - 895
    else:
        soul_amount = x * 75

    level_up_choice = input(f"Choose a stat to increase:\n"
                     f"Souls needed: {abs(int(soul_amount))}\n"
                     f"Current Souls: {player_stats['souls']}\n"
                     f"(1) Health\n"
                     f"(2) Attunement\n"
                     f"(3) Strength\n"
                     f"(4) Dexterity\n"
                     f"(5) Intelligence\n"
                     f"(6) Faith\n"
                     f"(7) Luck\n")
    stat_mapping = {
        '1': 'health',
        '2': 'attunement',
        '3': 'strength',
        '4': 'dexterity',
        '5': 'intelligence',
        '6': 'faith',
        '7': 'luck'
    }

    if player_stats['souls'] < int(soul_amount):
        print("Not enough souls to level up")
    else:
        if level_up_choice in stat_mapping:
            stat = stat_mapping[level_up_choice]
            player_stats[stat] += 1
            player_stats['level'] += 1
            player_stats['souls'] -= int(soul_amount)
            print(f"{player_name} leveled up! {stat} increased to {player_stats[stat]}")
        else:
            print("Invalid choice")

def player_death(player_name, player_stats, temp_stats):
    """Player death"""
    print(f"{player_name} has died!\n"
          f"{player_name} lost {player_stats['souls']} souls!\n")
    player_stats['souls'] -= round(player_stats['souls'] * .50)
    temp_stats['health'] = player_stats['health']
    temp_stats['attunement'] = player_stats['attunement']
    temp_stats['estus'] = player_stats['estus']
