"""Character information"""

from .professions import SELECT_PROFESSION
from .equipment import Equipment

def name_and_profession_selection():
    """Select player name and profession"""
    player_name = input("Please enter you name:\n").strip() or "Player"
    profession_list()

    while True:
        player_choice = input("Select a Profession:\n").strip().lower()

        # Validate input
        if player_choice in SELECT_PROFESSION:
            player_stats = SELECT_PROFESSION[player_choice].copy()
            print(f"Welcome, {player_name}! You have chosen {player_stats['name'].title()}.")
            return player_name, player_stats
        print("Invalid profession. Please choose a valid class.")
        print(", ".join(SELECT_PROFESSION.keys()))


def character_info(player_name, player_stats, temp_stats):
    """Display player information"""
    skills = get_player_stats(player_stats)
    equipment = player_stats['equipment']

    print(f"{player_name:<6} LVL: {skills['level']:<6}Total Souls: {skills['souls']:<6}")
    print(f"{'Profession':<14}"
          f"{'HP':<6}"
          f"{'MP':<6}"
          f"{'STR':<6}"
          f"{'DEX':<6}"
          f"{'INT':<6}"
          f"{'FAI':<6}"
          f"{'LCK':<6}"
          f"{'EST':<6}")
    print("-" * 65)
    print(f"{skills['name'].title():<14}"
          f"{skills['health']:<6}"
          f"{skills['attunement']:<6}"
          f"{skills['strength']:<6}"
          f"{skills['dexterity']:<6}"
          f"{skills['intelligence']:<6}"
          f"{skills['faith']:<6}"
          f"{skills['luck']:<6}"
          f"{skills['estus']:<6}\n")
    print("-" * 30)
    print(f"EQUIPPED:\n"
          f"Weapon: {equipment.weapon}\n"
          f"Armor: {equipment.armor}\n"
          f"Shield: {equipment.shield}")

    if equipment.rings:
        print("Rings:")
        for ring in equipment.rings:
            print(f"  - {ring}")
    else:
        print("Rings: None")

    if equipment.spells:
        print("Spells:")
        for spell in equipment.spells:
            print(f"  - {spell}")
    else:
        print("Spells: None")

def player_status(player_stats, temp_stats):
    """Display player status"""
    skills = get_player_stats(player_stats)
    equipment = player_stats['equipment']

    print("-" * 30)
    print(f"HP: {temp_stats['health']:<6}"
          f"MP: {temp_stats['attunement']:<6}\n"
          f"Estus Flasks: {temp_stats['estus']:<6}\n"
          f"Souls: {skills['souls']:<6}")
    print("-" * 30)
    if equipment.spells:
        print("Spells:")
        for spell in equipment.spells:
            print(f"  - {spell}")
    print("-" * 30 + "\n")

def profession_list():
    """Select player profession"""
    print(f"{'Profession':<14}"
          f"{'LVL':<6}"
          f"{'HP':<6}"
          f"{'MP':<6}"
          f"{'STR':<6}"
          f"{'DEX':<6}"
          f"{'INT':<6}"
          f"{'FAI':<6}"
          f"{'LCK':<6}"
          f"{'EST':<6}")
    print("-" * 65)

    for prof_select, skill in SELECT_PROFESSION.items():
        print(f"{prof_select:<3}"
              f"{skill['name'].title():<12}"
              f"{skill['level']:<6}"
              f"{skill['health']:<6}"
              f"{skill['attunement']:<6}"
              f"{skill['strength']:<6}"
              f"{skill['dexterity']:<6}"
              f"{skill['intelligence']:<6}"
              f"{skill['faith']:<6}"
              f"{skill['luck']:<6}"
              f"{skill['estus']:<6}")
    print("-" * 65)


def get_player_stats(player_stats):
    """Returns the player's stats for the selected profession"""
    return player_stats.copy()

def get_strongest_skill(skills):
    """Excludes 'health' and find the strongest skill"""
    ignore_health = {key: value for key, value in skills.items() if key not in(
        'name', 
        'health', 
        'attunement', 
        'estus', 
        'souls', 
        'rings', 
        'spells', 
        'equipment',
        'description',
        'luck'
        )}
    strong_skill = max(ignore_health, key=skills.get)
    return strong_skill
