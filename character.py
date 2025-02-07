"""Character information"""

from professions import SELECT_PROFESSION

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

    print(player_name)
    print(f"{'Profession':<16}{'HP':<6}{'STR':<6}{'DEX':<6}{'INT':<6}")
    print("-" * 60)
    print(f"{skills['name'].title():<16}"
          f"{skills['health']:<6}"
          f"{skills['strength']:<6}"
          f"{skills['dexterity']:<6}"
          f"{skills['intelligence']:<6}")
    print(f"Current health: {temp_stats['health']:<6}")

def profession_list():
    """Select player profession"""
    print(f"{'Profession':<12}"
          f"{'HP':<6}"
          f"{'STR':<6}"
          f"{'DEX':<6}"
          f"{'INT':<6}")
    print("-" * 60)

    for prof_select, skill in SELECT_PROFESSION.items():
        print(f"{prof_select:<2}"
              f"{skill['name'].title():<12}"
              f"{skill['health']:<6}"
              f"{skill['strength']:<6}"
              f"{skill['dexterity']:<6}"
              f"{skill['intelligence']:<6}")
    print("-" * 60)


def get_player_stats(player_stats):
    """Returns the player's stats for the selected profession"""
    return player_stats.copy()

def get_strongest_skill(skills):
    """Excludes 'health' and find the strongest skill"""
    ignore_health = {key: value for key, value in skills.items() if key not in('name', 'health')}
    strong_skill = max(ignore_health, key=skills.get)
    return strong_skill
