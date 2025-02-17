"""
Combat scenarios
"""
from .actions import (
    generate_enemy_encounter,
    player_death, player_combat_action,
    enemy_combat_action, who_attacks_first
)

def random_combat(player_name, player_stats, temp_stats):
    """Random combat encounter with a monster"""
    enemy = generate_enemy_encounter()
    who_attacks_first(player_name, player_stats, temp_stats, enemy)

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

        player_combat_action(player_name, player_stats, temp_stats, enemy)

        enemy_combat_action(player_name, temp_stats, enemy)
