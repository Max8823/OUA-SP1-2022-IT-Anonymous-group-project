import time

import pygame
import math

from Inventory import Inventory
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
        self.battle = False
        # track inventory open and item display open
        self.item_display_up = False
        self.inventory_open = False

# referencing level,
        self.level = level.Level

# used to pull chests into this class, preventing circular import
    def set_chest_list(self, chests):
        for chest in chests:
            self.chests.append(chest)

# used to load player into this class, preventing circular import
    def set_player(self, player):
        self.player = player

#used to pull items list from inventory when a change occurs back there
    def set_items(self, items_list):
        self.items_list = list()

        for items in items_list:
            self.items_list.append(items)

    # setting offset from level
    def set_offset(self, offset):
        self.offset = offset

    # pulling offset from level
    def get_offset(self):
        return self.offset

    # sending this bool variable to the Camera class in the 'Level' Class file so thye extra item information can be displayed
    def set_item_info(self, status):
        self.camera.set_item_info_status(status)

    def key_pressed(self, key):


        if key[pygame.K_p]:
            print(self.player.get_spell()["Fire Blast"]["damage"])



        # open invenventory
        if not self.inventory_open:
            if key[pygame.K_i]:
                self.clear_event()
                self.wait()
                self.camera.set_inven_status(True)
                self.inventory_open = True
                self.set_item_info(False)

        # this elif will close the item pop-up display if the user does not click on the 'X', requries both inventory and item display to be open
        elif self.inventory_open and self.item_display_up:
            if key[pygame.K_i]:
                self.clear_event()
                self.wait()
                self.set_item_info(False)
                self.item_display_up = False
        # will close inventory, if open and item display is not
        else:
            if key[pygame.K_i]:
                self.clear_event()
                self.wait()
                self.camera.set_inven_status(False)
                self.inventory_open = False
                self.set_item_info(False)

        # movement keys
        if key[pygame.K_w] or key[pygame.K_UP]:
            self.player.set_player_facing('up')
            self.player.set_player_direction_y(-1)
            self.player.normalise_player_direction_y('vertical')

        elif key[pygame.K_s] or key[pygame.K_DOWN]:
            self.player.set_player_facing('down')
            self.player.set_player_direction_y(1)
            self.player.normalise_player_direction_y('vertical')

        else:
            self.player.set_player_direction_y(0)

        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            self.player.set_player_facing('right')
            self.player.set_player_direction_x(1)
            self.player.normalise_player_direction_x('horizontal')

        elif key[pygame.K_a] or key[pygame.K_LEFT]:
            self.player.set_player_facing('left')
            self.player.set_player_direction_x(-1)
            self.player.normalise_player_direction_x('horizontal')

        else:
            self.player.set_player_direction_x(0)

        # if the player isn't in combat and not in battle, check for chests, can add other methods for doors, ect

        if pygame.mouse.get_pressed()[0]:
            self.clear_event()

            self.wait()
            self.check_mouse_click_left(pygame.mouse.get_pos())

        if pygame.mouse.get_pressed()[2]:
            self.clear_event()
            self.wait()
            mouse_pos = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
            self.check_mouse_click_right(mouse_pos)

    def check_mouse_click_left(self, mouse_pos):

        if not self.inventory_open or not self.battle:
            # this needs to be done because of re-sizing map
            mouse_pos_actual = mouse_pos[0] + self.get_offset()[0], mouse_pos[1] + \
                               self.get_offset()[1]
            self.check_chests(mouse_pos_actual)

        if self.inventory_open and self.item_display_up:

            # if clicked on cancel, close item display, from Camera and the tracker here
            if self.Inventory.get_cancel_pos().collidepoint(mouse_pos):
                self.item_display_up = False
                self.camera.set_item_info_status(False)

            # if clicked on equip - run equipping method/s
            if self.Inventory.get_second_button() == 1:
                if self.Inventory.get_display_equip_pos().collidepoint(mouse_pos):
                    print("equipping item calling goes here")

            # if clicked on 'use item' run use item method/s
            elif self.Inventory.get_second_button() == 2:
                if self.Inventory.get_display_use_item_pos().collidepoint(mouse_pos):
                    print("use item calling goes here")

    def check_mouse_click_right(self, mouse_pos):

        if self.inventory_open and not self.item_display_up:
            self.get_item_display(mouse_pos)

    def get_item_display(self, mouse_pos):
        i = 0

        for items in self.items_list:

            self.items_list[i].get_item_pos()

            item_pos_x = self.items_list[i].get_item_pos()[0]
            item_pos_y = self.items_list[i].get_item_pos()[1]

            if abs((((((item_pos_x + 55) - item_pos_x) / 2) + item_pos_x) - mouse_pos[0])) <= 30 and abs(
                    (((((item_pos_y + 55) - item_pos_y) / 2) + item_pos_y) - mouse_pos[1])) <= 30:

                self.Inventory.set_target_item(i)
                self.Inventory.draw_item_info()
                self.item_display_up = True
                self.set_item_info(True)

            else:
                i += 1

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

                    # might need to chaneg this sprite or something to an empty chest
                    self.chests.pop(i)
            i += 1

    def wait(self):
        pygame.time.wait(100)

    def clear_event(self):
        pygame.event.clear()
