import time

import pygame
import math
import level

from Inventory import Inventory
from battle import battle
from math import *


class user_interactions():
    def __init__(self):

        self.keys = pygame.key.get_pressed()
        self.Inventory = Inventory()
        self.player = object
        self.items_list = []
        self.equipped_items = []
        self.chests = []
        self.enemies = []
        self.in_battle = False
        self.battle = battle()
        # track inventory open and item display open
        self.inventory_open = False
        self.loaded = False

        # referencing level,
        self.level = level
        self.camera = level.Camera()
        self.map_num = None
        self.spells_pos = self.Inventory.get_spell_pos()
        self.equipped_items_pos = self.Inventory.get_equipped_items_pos()
        self.battle_result = True

        self.battle.set_result(True)

    # used to pull chests into this class, preventing circular import
    def set_chest_list(self, chests):
        for chest in chests:
            self.chests.append(chest)

    # used to load player into this class, preventing circular import
    def set_player(self, player):
        self.player = player
        self.Inventory.add_item(0, 2)
        self.set_items(self.Inventory.get_items_list())
        self.update_inventory()


    # used to pull items list from inventory when a change occurs back there
    def set_items(self, items_list):
        self.items_list = list()

        for items in items_list:
            self.items_list.append(items)

    def set_equipped_items(self, equipped_items):
        self.equipped_items = list()

        for items in equipped_items:
            self.equipped_items.append(items)

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

    def set_equip_info(self, status):
        self.camera.set_equip_info_status(status)

    def set_loaded(self, set):
        self.loaded = set

    def get_loaded(self):
        return self.loaded

    def set_map_num(self, map_num):
        self.map_num = map_num

    def get_map_num(self):
        return self.map_num

    def key_pressed(self, key):

        # open invenventory

        if self.get_loaded():

            # this is a testing method, used for cancelling combat
            if key[pygame.K_p]:
                self.wait()
                self.battle.end_battle(True)
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

            if self.in_battle:
                if pygame.mouse.get_pressed()[0]:
                    mouse_pos = pygame.mouse.get_pos()
                    self.check_exit(mouse_pos)
                    self.check_potions(mouse_pos)



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
            else:
                battle_status = self.battle.get_battle_status()
                if not battle_status:
                    self.in_battle = False
                    self.battle.set_battle_status(False)
                    self.set_battle_status(self.battle.get_result())

            # if the player isn't in combat and not in battle, check for chests, can add other methods for doors, ect

            if pygame.mouse.get_pressed()[0]:
                self.wait()
                self.check_mouse_click_left(pygame.mouse.get_pos())

            if pygame.mouse.get_pressed()[2]:
                mouse_pos = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
                self.check_mouse_click_right(mouse_pos)

    def set_battle_status(self, result_of_battle):
        self.battle_result = result_of_battle

    def get_battle_result(self):

        return self.battle_result

    def reset_all(self):
        self.set_battle_status(True)
        self.player.reset_player()
        self.Inventory.reset_inven()


    def check_mouse_click_left(self, mouse_pos):

        if not self.inventory_open:
            # this needs to be done because of re-sizing map
            mouse_pos_actual = mouse_pos[0] + self.get_offset()[0], mouse_pos[1] + \
                               self.get_offset()[1]
            self.check_chests(mouse_pos_actual)

        if self.inventory_open and self.Inventory.get_equip_display_up():

            if self.Inventory.get_cancel_pos().collidepoint(mouse_pos):
                self.Inventory.set_equip_display_up(False)
                self.camera.set_equip_info_status(False)

            if self.Inventory.get_display_unequip_pos().collidepoint(mouse_pos):
                self.Inventory.set_equip_display_up(False)
                self.camera.set_equip_info_status(False)
                self.Inventory.remove_equipped_item(self.equipped_items[self.Inventory.get_target_item()])
                self.update_inventory()


        elif self.inventory_open and self.Inventory.get_item_display_up():

            # if clicked on cancel, close item display, from Camera and the tracker here
            if self.Inventory.get_cancel_pos().collidepoint(mouse_pos):
                self.Inventory.set_item_display_up(False)
                self.camera.set_item_info_status(False)

            # if clicked on equip - run equipping method/s
            if self.Inventory.get_second_button() == 1:
                if self.Inventory.get_display_equip_pos().collidepoint(mouse_pos):
                    # remove print
                    self.Inventory.set_item_display_up(False)
                    self.camera.set_item_info_status(False)
                    self.Inventory.equip_item(self.items_list[self.Inventory.get_target_item()])
                    self.update_inventory()

            # if clicked on 'use item' run use item method/s
            elif self.Inventory.get_second_button() == 2:

                ############
                if self.Inventory.get_display_use_item_pos().collidepoint(mouse_pos):

                    if self.items_list[self.Inventory.get_target_item()].get_item_code() == 0:
                        self.player.heal_player(100)
                        self.Inventory.consume_item()
                        self.update_inventory()

                    elif self.items_list[self.Inventory.get_target_item()].get_item_code() == 8:
                        self.player.increase_max_health()
                        self.Inventory.consume_item()
                        self.update_inventory()

                    elif self.items_list[self.Inventory.get_target_item()].get_item_code() in range(4, 8, 1):
                        self.player.update_spell(self.items_list[self.Inventory.get_target_item()].get_item_name(),
                                                 "True")
                        self.Inventory.consume_item()
                        spells = self.player.get_player_spells()
                        self.Inventory.set_spells(spells)
                        self.update_inventory()

    def update_inventory(self):
        self.set_equipped_items(self.Inventory.get_equipped_items())
        self.set_items(self.Inventory.get_items_list())

    def check_mouse_click_right(self, mouse_pos):

        if self.inventory_open and not self.Inventory.get_item_display_up() and not self.Inventory.get_spell_display_up() and not self.Inventory.get_equip_display_up():
            if mouse_pos[0] < 600:
                self.get_spell_display(mouse_pos)
            else:
                if mouse_pos[1] < 460:
                    self.get_item_display(mouse_pos)
                else:
                    self.get_equipped_display(mouse_pos)

    def check_for_enemies(self):

        i = 0
        for enemy in self.enemies:

            if math.floor(dist((sqrt((pow(self.player.get_player_pos()[0] - 0, 2))),
                                sqrt((pow(self.player.get_player_pos()[1] - 0, 2)))), self.enemies[i].enemy_pos)) <= 64:

                self.battle.set_battle(self.player, self.enemies[i], self.get_map_num())
                self.in_battle = True
                self.battle.set_battle_status(True)
                self.match = True

            else:
                i+=1


    def check_exit(self, mouse_pos):

        i = 0
        item_pos_x = 20
        item_pos_y = 500

        if abs((((((item_pos_x + 150) - item_pos_x) / 2) + item_pos_x) - mouse_pos[0])) <= 50 and abs(
                (((((item_pos_y + 100) - item_pos_y) / 2) + item_pos_y) - mouse_pos[1])) <= 75:

            self.battle.end_battle(True)
            self.in_battle = False
            self.battle.set_battle_status(False)
            self.battle.set_turn()

        else:
               ''
    def check_potions(self, mouse_pos):

        i = 0
        item_pos_x = 30
        item_pos_y = 375

        if abs((((((item_pos_x + 55) - item_pos_x) / 2) + item_pos_x) - mouse_pos[0])) <= 27.5 and abs(
                (((((item_pos_y + 55) - item_pos_y) / 2) + item_pos_y) - mouse_pos[1])) <= 27.5:

            for item in self.items_list:

                if self.items_list[i].get_item_code() == 0:
                    self.Inventory.set_target_item(i)
                    self.player.heal_player(100)
                    self.Inventory.consume_item()
                    self.update_inventory()
                else:
                    i+=1
        else:
               ''


    def change_map_level(self):

        if math.floor(dist((sqrt((pow(self.player.get_player_pos()[0] - 0, 2))),
                            sqrt((pow(self.player.get_player_pos()[1] - 0, 2)))),
                           self.level.Portal.get_position())) <= 32:

            if self.get_map == 0:

                self.level.Camera.set_map(1)
                self.level.Level.load_map(1)
                self.Inventory.temporary_inventory()

                if self.get_map == 1:
                    self.Inventory.switch_to_original_inven()

            elif self.get_map == 1:

                self.level.Camera.set_map(2)
                self.level.Level.load_map(2)
                self.Inventory.temporary_inventory()

                if self.get_map == 2:
                    self.Inventory.switch_to_original_inven()

            else:
                ''

    def get_equipped_display(self, mouse_pos):

        self.equipped_items_pos = self.Inventory.get_equipped_items_pos()
        i = 0
        j = 0
        for item in self.equipped_items_pos:
            pos = self.equipped_items_pos[i]
            posx = pos[0]
            posy = pos[1]

            if abs((((((posx + 55) - posx) / 2) + posx) - mouse_pos[0])) <= 30 and abs(
                    (((((posy + 55) - posy) / 2) + posy) - mouse_pos[1])) <= 30:

                self.Inventory.set_target_item(j)
                self.Inventory.draw_equip_info()
                self.Inventory.set_equip_display_up(True)
                self.set_equip_info(True)

            else:
                i += 1
                j += 1

    def get_spell_display(self, mouse_pos):
        MatchFound = False
        i = 0
        for spell in self.spells_pos:
            pos = self.spells_pos[i][0]
            posx = pos[0]
            posy = pos[1]

            if abs((((((posx + 55) - posx) / 2) + posx) - mouse_pos[0])) <= 55 and abs(
                    (((((posy + 55) - posy) / 2) + posy) - mouse_pos[1])) <= 55:

                self.Inventory.set_taregt_spell(self.spells_pos[i][1])
                self.Inventory.draw_spell_info()
                self.Inventory.set_spell_display_up(True)
                self.set_spell_info(True)
                MatchFound = True

            else:
                i += 1

        return MatchFound

    def get_item_display(self, mouse_pos):
        i = 0
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
                    self.Inventory.add_item(0, 2)

                    self.set_items(self.Inventory.get_items_list())

                    # might need to change this sprite or something to an empty chest
                    self.chests.pop(i)
            i += 1

    def wait(self):
        pygame.time.wait(100)

    def clear_event(self):
        pygame.event.clear()
