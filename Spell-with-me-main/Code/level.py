import threading

import pygame

from config import *
from tile import Tile
from player import Player
from Chest import Chest
from Inventory import Inventory
import user_interactions

inven_open = False
item_info = False


class Level:
    def __init__(self):

        self.chests = []

        # get the display surface this is where objects are drawn
        self.display_surface = pygame.display.get_surface()

        # sprite group setup, camera this method re-draws the map when moving around
        self.visible_sprites = Camera()
        # obstale and chest sprites, chests are both an obstacle and a chest. this is done to make chests interactive, same thing can be done with doors, ladders, ect
        self.obstacle_sprites = pygame.sprite.Group()
        self.chest_sprites = pygame.sprite.Group()
        self.item_sprites = pygame.sprite.Group()

        self.user_action = user_interactions.user_interactions()

        # creating the map
        self.load_map(MAP1)


    def load_map(self, map):
        # background here

        for row_index, row in enumerate(map):
            for col_index, col in enumerate(row):

                x = col_index * TILESIZE
                y = row_index * TILESIZE

                # dont worry about any of the highlited things below: they wont throw errors
                if col == 'x':
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'boundry')

                if col == 'p':
                    self.player = Player(x, y, [self.visible_sprites], self.obstacle_sprites)

                if col == 'c':
                    Tile((x, y), [self.visible_sprites, self.chest_sprites, self.obstacle_sprites], 'chest')
                    self.chests.append(Chest(x, y))

        # passing the player and the chests list to the user action menu so they can be sued there
        self.user_action.set_chest_list(self.chests)
        self.user_action.set_player(self.player)

    def run(self):
        # update and draw the game

        self.visible_sprites.draw_all(self.player)
        self.visible_sprites.update()

        self.keys = pygame.key.get_pressed()
        self.user_action.key_pressed(self.keys)
        self.user_action.set_offset(self.visible_sprites.get_offset())


# this is for the adjusting of the screen how the camera follows it around
class Camera(pygame.sprite.Group):
    def __init__(self):
        # general setup
        super().__init__()
        self.Inventory = Inventory()

        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] / 2
        self.half_height = self.display_surface.get_size()[1] / 2
        self.offset = pygame.math.Vector2()

    # passing the map offset which is calculated by dividing the map x,y /2 respectively and putting them into a Vector (x:y) ^^
    def get_offset(self):

        return self.offset

    # setting the inventory_open flag for drawing hte inventory
    def set_inven_status(self, status):
        global inven_open

        inven_open = status

    def set_item_info_status(self, status):
        global item_info

        item_info = status

    # includes drawing inventory
    def draw_all(self, player):
        # getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        if inven_open:

            if item_info:

                self.draw_sprites()
                self.Inventory.draw_inven()
                self.Inventory.draw_item_info()


            else:

                self.draw_sprites()
                self.Inventory.draw_inven()

        else:
            self.draw_sprites()

    # draws map sprites only, no inventory stuff drawn here
    def draw_sprites(self):

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
