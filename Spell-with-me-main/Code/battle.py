import pygame
from player import *
from Inventory import Inventory
from enemy_class import *
import Item
import level
import config

battle_status = False
player = object
enemy = object

class battle:
    def __init__(self):

        self.player = object
        self.enemy = object
        self.loot = None
        self.turn = 'player'
        self.result = False
        self.map0_background = pygame.image.load('../graphics/maps/0/battle_scene.png').convert_alpha()


        self.screen = pygame.display.get_surface()

    def set_battle(self, player1, enemy1, map_code):
        global player, enemy

        player = player1
        enemy = enemy1
        self.map_code = map_code

    def set_battle_status(self, status):
        global battle_status
        battle_status = status

    def get_battle_status(self):
        global battle_status
        return battle_status


    def end_battle(self):
        global battle_status
        battle_status = False

        self.set_battle_loot(enemy.get_loot())
        pygame.sprite.Sprite.kill(enemy)

        self.set_result(True)

        #will shove enemy to 0:0
        enemy.set_enemy_pos()

    def set_battle_loot(self, loot):
        loot_list = list(loot)
        player_known = player.get_player_learned_spells()
        while loot_list[0] in player_known:

            loot_list[0] = random.randrange(0, 9, 1)

        self.loot = loot_list



    def get_battle_loot(self):
        return self.loot

    def get_result(self):
        return self.result

    def set_result(self, result):
        self.result = result

    def draw_battle(self):
        #chaneg to background image / could be random 1 of 3? or 1 per map?


            self.screen.blit(self.map0_background, (0,0))

            self.screen.blit(player.get_player_image(), (450, 550))
            self.screen.blit(enemy.get_enemy_image(), (500, 500))




