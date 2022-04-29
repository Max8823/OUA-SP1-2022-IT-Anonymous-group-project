import time

import pygame
import math

from Inventory import Inventory
from battle import battle
import level
from math import *


class user_interactions():
    def __init__(self):

        self.keys = pygame.key.get_pressed()
        self.Inventory = Inventory()
        self.camera = level.Camera()
        self.player = object
        self.items_list = []
        self.chests = []
        self.enemies = []
        self.in_battle = False
        self.battle = battle()
        # track inventory open and item display open
        self.inventory_open = False
        self.loaded = False

        # referencing level,
        self.level = level.Level
        self.spells_pos = self.Inventory.get_spell_pos()

    # used to pull chests into this class, preventing circular import
    def set_chest_list(self, chests):
        for chest in chests:
            self.chests.append(chest)

    # used to load player into this class, preventing circular import
    def set_player(self, player):
        self.player = player

    # used to pull items list from inventory when a change occurs back there
    def set_items(self, items_list):
        self.items_list = list()

        for items in items_list:
            self.items_list.append(items)

    def set_enemies(self, enemies):
        for enemy in enemies:
            self.enemies.append(enemy)

    # setting offset from level
    def set_offset(self, offset):
        self.offset = offset

    # pulling offset from level
    def get_offset(self):
        return self.offset

    # sending this bool variable to the Camera class in the 'Level' Class file so thye extra item information can be displayed
    def set_item_info(self, status):
        self.camera.set_item_info_status(status)

    def set_spell_info(self, status):
        self.camera.set_spell_info_status(status)

    def set_loaded(self, set):
        self.loaded = set

    def get_loaded(self):
        return self.loaded

    def key_pressed(self, key):

        # open invenventory

        if self.get_loaded():

            # this is a testing method, used for cancelling combat
            if key[pygame.K_p]:
                self.wait()
                self.battle.end_battle()
                self.in_battle = False
                self.Inventory.add_item(self.battle.get_battle_loot()[0], self.battle.get_battle_loot()[1])
                self.set_items(self.Inventory.get_items_list())




            if not self.inventory_open:
                if key[pygame.K_i]:
                    self.wait()
                    self.camera.set_inven_status(True)
                    self.inventory_open = True
                    spells = self.player.get_player_spells()
                    self.Inventory.set_spells(spells)
                    self.set_item_info(False)


            # this elif will close the item pop-up display if the user does not click on the 'X', requries both inventory and item display to be open
            elif self.inventory_open and self.Inventory.get_item_display_up():
                if key[pygame.K_i]:
                    self.clear_event()
                    self.wait()
                    self.set_item_info(False)
                    self.Inventory.set_item_display_up(False)

            elif self.inventory_open and self.Inventory.get_spell_display_up():
                if key[pygame.K_i]:
                    self.clear_event()
                    self.wait()
                    self.set_spell_info(False)
                    self.Inventory.set_spell_display_up(False)

            # will close inventory, if open and item display is not
            else:
                if key[pygame.K_i]:
                    self.clear_event()
                    self.wait()
                    self.camera.set_inven_status(False)
                    self.inventory_open = False
                    self.Inventory.set_item_display_up(False)
                    self.set_item_info(False)

            if not self.in_battle:
                # movement keys
                if key[pygame.K_w] or key[pygame.K_UP]:
                    self.player.set_player_facing('up')
                    self.player.set_player_direction_y(-1)
                    self.player.normalise_player_direction_y('vertical')
                    self.check_for_enemies()

                elif key[pygame.K_s] or key[pygame.K_DOWN]:
                    self.player.set_player_facing('down')
                    self.player.set_player_direction_y(1)
                    self.player.normalise_player_direction_y('vertical')
                    self.check_for_enemies()

                else:
                    self.player.set_player_direction_y(0)

                if key[pygame.K_d] or key[pygame.K_RIGHT]:
                    self.player.set_player_facing('right')
                    self.player.set_player_direction_x(1)
                    self.player.normalise_player_direction_x('horizontal')
                    self.check_for_enemies()

                elif key[pygame.K_a] or key[pygame.K_LEFT]:
                    self.player.set_player_facing('left')
                    self.player.set_player_direction_x(-1)
                    self.player.normalise_player_direction_x('horizontal')
                    self.check_for_enemies()

                else:
                    self.player.set_player_direction_x(0)

            # if the player isn't in combat and not in battle, check for chests, can add other methods for doors, ect

            if pygame.mouse.get_pressed()[0]:
                self.wait()
                self.check_mouse_click_left(pygame.mouse.get_pos())

            if pygame.mouse.get_pressed()[2]:

                mouse_pos = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
                self.check_mouse_click_right(mouse_pos)

    def check_mouse_click_left(self, mouse_pos):

        if not self.inventory_open:
            # this needs to be done because of re-sizing map
            mouse_pos_actual = mouse_pos[0] + self.get_offset()[0], mouse_pos[1] + \
                               self.get_offset()[1]
            self.check_chests(mouse_pos_actual)

        if self.inventory_open and self.Inventory.get_item_display_up():

            # if clicked on cancel, close item display, from Camera and the tracker here
            if self.Inventory.get_cancel_pos().collidepoint(mouse_pos):
                self.Inventory.set_item_display_up(False)
                self.camera.set_item_info_status(False)


            # if clicked on equip - run equipping method/s
            if self.Inventory.get_second_button() == 1:
                if self.Inventory.get_display_equip_pos().collidepoint(mouse_pos):
                    # remove print
                    self.Inventory.equip_item(self.items_list[self.Inventory.get_target_item()].get_item_code())

            # if clicked on 'use item' run use item method/s
            elif self.Inventory.get_second_button() == 2:

                ############
                if self.Inventory.get_display_use_item_pos().collidepoint(mouse_pos):


                    if self.items_list[self.Inventory.get_target_item()].get_item_code() == 0:
                        self.player.heal_player(100)
                        self.Inventory.consume_item()

                    elif self.items_list[self.Inventory.get_target_item()].get_item_code() == 8:
                        self.player.increase_max_health()
                        self.Inventory.consume_item()

                    elif self.items_list[self.Inventory.get_target_item()].get_item_code() in range(4, 8, 1):
                        self.player.update_spell(self.items_list[self.Inventory.get_target_item()].get_item_name(),
                                                 "True")
                        self.Inventory.consume_item()
                        spells = self.player.get_player_spells()
                        self.Inventory.set_spells(spells)

    def check_for_enemies(self):

        i=0
        for enemy in self.enemies:

            if math.floor(dist((sqrt((pow(self.player.get_player_pos()[0] - 0, 2))),
                                sqrt((pow(self.player.get_player_pos()[1] - 0, 2)))), self.enemies[i].enemy_pos)) <= 64:

                self.battle.set_battle(self.player, self.enemies[i])
                self.in_battle = True
                self.battle.set_battle_status(True)

                if not self.in_battle:

                    if self.battle.get_result():

                        self.battle.end_battle()
                        self.in_battle = False
                        self.Inventory.add_item(self.battle.get_battle_loot()[0], self.battle.get_battle_loot()[1])
                        self.set_items(self.Inventory.get_items_list())


                    else:
                        pygame.sprite.Sprite.kill(self.player)




            else:
                i += 1
                self.in_battle = False

    def check_mouse_click_right(self, mouse_pos):

        if self.inventory_open and not self.Inventory.get_item_display_up() and not self.Inventory.get_spell_display_up():
            if not self.get_item_display(mouse_pos):
                self.get_spell_display(mouse_pos)



    def get_spell_display(self, mouse_pos):

        i=0
        for spell in self.spells_pos:
            pos = self.spells_pos[i][0]
            posx = pos[0]
            posy = pos[1]

            if abs((((((posx + 55) - posx) / 2) + posx) - mouse_pos[0])) <= 30 and abs(
                    (((((posy + 55) - posy) / 2) + posy) - mouse_pos[1])) <= 30:

                self.Inventory.set_taregt_spell(self.spells_pos[i][1])
                self.Inventory.draw_spell_info()
                self.Inventory.set_spell_display_up(True)
                self.set_spell_info(True)


            else:
                i+=1


    def get_item_display(self, mouse_pos):
        i = 0
        spells_pos = self.Inventory.get_spell_pos()
        MatchFound = False

        for items in self.items_list:

            self.items_list[i].get_item_pos()

            item_pos_x = self.items_list[i].get_item_pos()[0]
            item_pos_y = self.items_list[i].get_item_pos()[1]

            if abs((((((item_pos_x + 55) - item_pos_x) / 2) + item_pos_x) - mouse_pos[0])) <= 30 and abs(
                    (((((item_pos_y + 55) - item_pos_y) / 2) + item_pos_y) - mouse_pos[1])) <= 30:

                self.Inventory.set_target_item(i)
                self.Inventory.draw_item_info()
                self.Inventory.set_item_display_up(True)
                self.set_item_info(True)
                MatchFound = True

            else:
                i += 1

        return MatchFound
    # checking all the chests on the current map
    def check_chests(self, mouse_pos):

        i = 0
        for chest in self.chests:

            if dist(mouse_pos, self.chests[i].get_chest_pos()) <= 64:

                # checking if player is close enough to the item
                if math.floor(dist((sqrt((pow(self.player.get_player_pos()[0] - 0, 2))),
                                    sqrt((pow(self.player.get_player_pos()[1] - 0, 2)))),
                                   self.chests[i].get_chest_pos())) <= 64:
                    self.Inventory.add_item(self.chests[i].get_chest_contents()[0],
                                            self.chests[i].get_chest_contents()[1])

                    self.set_items(self.Inventory.get_items_list())

                    # might need to change this sprite or something to an empty chest
                    self.chests.pop(i)
            i += 1

    def wait(self):
        pygame.time.wait(100)

    def clear_event(self):
        pygame.event.clear()
