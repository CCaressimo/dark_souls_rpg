"""
Old school rpg with conditionals.
"""

from src.character.character import name_and_profession_selection, get_player_stats
from src.combat.actions import rest_at_bonfire
from src.combat.combat import random_combat

player_name, player_stats = name_and_profession_selection()
temp_stats = get_player_stats(player_stats)
while True:
    if int(temp_stats['health']) > 0:
        print(f"{player_name} travels to the next area...")
    else:
        rest_at_bonfire(player_name, player_stats, temp_stats)
    random_combat(player_name, player_stats, temp_stats)
    random_combat(player_name, player_stats, temp_stats)
    rest_at_bonfire(player_name, player_stats, temp_stats)
