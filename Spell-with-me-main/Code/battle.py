import pygame
import Inventory
import player
import enemy_class


class battle:
    def __init__(self, player, enemy):
        self.item_display_up = False
        self.inventory_open = False

        self.enemy = enemy
        self.player = player
        self.screen = pygame.display.get_surface()


    def set_battle(self, player, enemy):
        self.enemy = enemy
        self.player = player

    def get_battle_players(self):
        return self.enemy, self.player

    def draw_arena(self):
        self.screen.fill('white')
        self.get_battle_players()
        self.player = self.get_battle_players()[1]
        self.enemy = self.get_battle_players()[0]
        print(self.player.get_player_pos())

        print(self.player, self.enemy)


