class Enemy:
    player_spells = {
        "Inferno": 1,
        "Mind Control": 2,
        "Dark Mist": 2,
        "Terrify": 2
    }

    def __init__(self, name, health, spell):
        self.__name = name
        self.__health = health
        self.__spell = self.player_spells[spell]

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = value

    @property
    def spell(self):
        return self.__spell

    @spell.setter
    def spell(self, value):
        self.__spell = self.player_spells[value]
