"""
Professions for the game
"""

from .equipment import Equipment

SELECT_PROFESSION = {
    "1":{
        "name": "knight",
        "description": "An obscure knight of poor renown who collapsed roaming the land. "
                        "Sturdy, owing to high vitality and stout armor.",
        "equipment": Equipment(
            weapon="longsword",
            armor="knight armor",
            shield="knight shield",
            rings=[],
            spells=[]
            ),
        "level": 9,
        "health": 12,
        "attunement": 10,
        "strength": 13,
        "dexterity": 12,
        "intelligence": 9,
        "faith": 9,
        "luck": 7,
        "estus": 5,
        "souls": 0
    },
    "2":{
        "name": "mercenary",
        "description": "A mercenary and veteran of the battlefield. "
                        "High dexterity allows masterful wielding of dual scimitars.",
        "equipment": Equipment(
            weapon="sellsword twinblades",
            armor="sellsword armor",
            shield="wooden shield",
            rings=[],
            spells=[]
            ),
        "level": 8,
        "health": 11,
        "attunement": 12,
        "strength": 10,
        "dexterity": 16,
        "intelligence": 10,
        "faith": 8,
        "luck": 9,
        "estus": 5,
        "souls": 0
    },
    "3":{
        "name": "warrior",
        "description": "Descendant of northern warriors famed for their brawn. "
                        "Utilizes high strength to wield a heavy battleaxe.",
        "equipment": Equipment(
            weapon="battleaxe",
            armor="northern armor",
            shield="round shield",
            rings=[],
            spells=[]
            ),
        "level": 7,
        "health": 14,
        "attunement": 6,
        "strength": 16,
        "dexterity": 9,
        "intelligence": 8,
        "faith": 9,
        "luck": 11,
        "estus": 5,
        "souls": 0
    },
    "4":{
        "name": "herald",
        "description": "A former herald who journeyed to finish a quest undertaken. "
                        "Wields a sturdy spear and employs a gentle restorative miracle.",
        "equipment": Equipment(
            weapon="spear",
            armor="herald armor",
            shield="kite shield",
            rings=[],
            spells=[]
            ),
        "level": 9,
        "health": 12,
        "attunement": 10,
        "strength": 9,
        "dexterity": 11,
        "intelligence": 8,
        "faith": 13,
        "luck": 11,
        "estus": 5,
        "souls": 0
    },
    "5":{
        "name": "thief",
        "description": "A common thief and pitiful deserter. "
                        "Wields a dagger intended for backstabs.",
        "equipment": Equipment(
            weapon="bandit dagger",
            armor="deserter armor",
            shield="iron round shield",
            rings=[],
            spells=[]
            ),
        "level": 5,
        "health": 4,
        "attunement": 11,
        "strength": 7,
        "dexterity": 6,
        "intelligence": 6,
        "faith": 8,
        "luck": 10,
        "estus": 5,
        "souls": 0
    },
    "6":{
        "name": "assassin",
        "description": "An assassin who stalks their prey from the shadows. "
                        "Favors sorceries in addition to thrusting swords.",
        "equipment": Equipment(
            weapon="estoc",
            armor="assassin armor",
            shield="target shield",
            rings=[],
            spells=['spook']
            ),
        "level": 10,
        "health": 10,
        "attunement": 10,
        "strength": 10,
        "dexterity": 14,
        "intelligence": 11,
        "faith": 9,
        "luck": 10,
        "estus": 5,
        "souls": 0
    },
    "7":{
        "name": "hunter",
        "description": "A hunter who stalks their prey from the shadows. "
                        "Skilled with a bow and arrow.",
        "equipment": Equipment(
            weapon="short bow",
            armor="leather armor",
            shield="leather shield",
            rings=[],
            spells=[]
            ),
        "level": 7,
        "health": 10,
        "attunement": 12,
        "strength": 7,
        "dexterity": 18,
        "intelligence": 10,
        "faith": 8,
        "luck": 12,
        "estus": 5,
        "souls": 0
    },
    "8":{
        "name": "sorcerer",
        "description": "A loner who left formal academia to pursue further research. "
                        "Commands soul sorceries using high intelligence.",
        "equipment": Equipment(
            weapon="mail breaker",
            armor="sorcerer robe",
            shield="sorcerer shield",
            rings=['young dragon ring'],
            spells=['soul arrow', 'heavy soul arrow']
            ),
        "level": 6,
        "health": 9,
        "attunement": 16,
        "strength": 7,
        "dexterity": 12,
        "intelligence": 16,
        "faith": 7,
        "luck": 12,
        "estus": 5,
        "souls": 0
    },
    "9":{
        "name": "pyromancer",
        "description": "A pyromancer from a remote region who manipulates flame. "
                        "Also an adept close combat warrior who wields a hand axe.",
        "equipment": Equipment(
            weapon="hand axe",
            armor="pyromancer robe",
            shield="round shield",
            rings=['great swamp ring'],
            spells=['fire ball']
            ),
        "level": 8,
        "health": 11,
        "attunement": 12,
        "strength": 12,
        "dexterity": 9,
        "intelligence": 14,
        "faith": 14,
        "luck": 7,
        "estus": 5,
        "souls": 0
    },
    "10":{
        "name": "cleric",
        "description": "A traveling cleric who collapsed from exhaustion. "
                        "Channels high faith to cast many and varied miracles.",
        "equipment": Equipment(
            weapon="mace",
            armor="cleric robe",
            shield="wooden shield",
            rings=[],
            spells=['heal', 'force']
            ),
        "level": 7,
        "health": 10,
        "attunement": 14,
        "strength": 7,
        "dexterity": 8,
        "intelligence": 7,
        "faith": 16,
        "luck": 13,
        "estus": 5,
        "souls": 0
    },
    "11":{
        "name": "deprived",
        "description": "Naked and of unknown origin. "
                        "Either an unimaginable fool in life, "
                        "or was stripped of possessions upon burial.",
        "equipment": Equipment(
            weapon="club",
            armor="",
            shield="loincloth",
            rings=[],
            spells=[]
            ),
        "level": 1,
        "health": 10,
        "attunement": 10,
        "strength": 10,
        "dexterity": 10,
        "intelligence": 10,
        "faith": 10,
        "luck": 10,
        "estus": 5,
        "souls": 0
    }
}
