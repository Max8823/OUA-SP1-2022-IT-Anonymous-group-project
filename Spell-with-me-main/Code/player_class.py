class Player:
    player_spells = {
        "Fire Blast": 1,
        "Water Blast": 1,
        "Earth Blast": 1,
        "Wind Blast": 1
        "Fire Fury": 3,
        "Water Fury": 3,
        "Earth Fury": 3,
        "Wind Fury": 3,
    }

    def __init__(self, name, spell):

        self.__name = name
        self.__health = 5
        self.__spell = self.player_spells[spell]

    @property
    def name(self):
        return self.__name

    @property
    def spell(self):
        return self.__spell

    @spell.setter
    def spell(self, value):
        self.__spell = self.player_spells[value]
