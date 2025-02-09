"""
Player equipment and inventory
"""

class Equipment:
    """Defines player's equipment"""
    MAX_RINGS = 2
    MAX_SPELLS = 3

    def __init__(self, weapon="None",
                armor="None", shield="None",
                rings=None, spells=None, **kwargs):
        self.weapon = weapon
        self.armor = armor
        self.shield = shield
        # Use _rings and _spells for internal storage
        self._rings = []
        self._spells = []

        # Initialize with starting rings and spells
        if rings:
            for ring in rings[:self.MAX_RINGS]:
                self.add_ring(ring)
        if spells:
            for spell in spells[:self.MAX_SPELLS]:
                self.add_spell(spell)

    def add_ring(self, ring):
        """Add a ring if under the limit"""
        if len(self._rings) < self.MAX_RINGS:
            self._rings.append(ring)
            return True
        return False

    def remove_ring(self, ring):
        """Remove a specific ring"""
        if ring in self._rings:
            self._rings.remove(ring)
            return True
        return False

    def add_spell(self, spell):
        """Add a spell if under the limit"""
        if len(self._spells) < self.MAX_SPELLS:
            self._spells.append(spell)
            return True
        return False

    def remove_spell(self, spell):
        """Remove a specific spell"""
        if spell in self._spells:
            self._spells.remove(spell)
            return True
        return False

    @property
    def rings(self):
        """Get the list of rings (read-only)"""
        return self._rings.copy()

    @property
    def spells(self):
        """Get the list of spells (read-only)"""
        return self._spells.copy()

    def to_dict(self):
        """Convert equipment to dictionary format"""
        return {
            "weapon": self.weapon,
            "armor": self.armor,
            "shield": self.shield,
            "rings": self._rings.copy(),
            "spells": self._spells.copy()
        }
