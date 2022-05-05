import threading

import pygame, sys, threading, re

sys.path.append('../Loading_screen/loading_screen')
from config import *
from tile import Tile
from player import Player
from Chest import Chest
from Inventory import Inventory
import user_interactions
from enemy_class import Enemy
from asset_loader import *
from battle import *

from random import choice, randint

inven_open = False
item_info = False
spell_info = False
equip_info = False



class Level:
    def __init__(self):

        self.chests = []
        self.enemies = []

        # get the display surface this is where objects are drawn
        self.display_surface = pygame.display.get_surface()

        # sprite group setup, camera this method re-draws the map when moving around
        self.visible_sprites = Camera()
        # obstale and chest sprites, chests are both an obstacle and a chest. this is done to make chests interactive, same thing can be done with doors, ladders, ect
        self.obstacle_sprites = pygame.sprite.Group()

        self.background_sprites = pygame.sprite.Group()
        self.chest_sprites = pygame.sprite.Group()
        self.item_sprites = pygame.sprite.Group()

        self.user_action = user_interactions.user_interactions()
        self.loaded_img = False
        self.play = False
        self.loaded = False

        # creating the map



    def start_screen(self):
        if not self.loaded_img:
            self.load_start_screen_img()

        background_rect = self.start_background.get_rect()
        self.display_surface.blit(self.start_background, background_rect)

        play_button_rect = self.play_button.get_rect()
        play_button_rect.center = background_rect.center[0], background_rect.center[1]
        self.display_surface.blit(self.play_button, play_button_rect)

        instructions_rect = self.instructions_button.get_rect()
        instructions_rect.center = background_rect.center[0], play_button_rect.center[1] + 75
        self.display_surface.blit(self.instructions_button, instructions_rect)

        quit_rect = self.quit_button.get_rect()
        quit_rect.center = background_rect.center[0], instructions_rect.center[1] + 75
        self.display_surface.blit(self.quit_button, quit_rect)

        if pygame.mouse.get_pressed()[0]:
            pygame.event.clear(pygame.mouse.get_pressed())

            mouse_pos = pygame.mouse.get_pos()

            if play_button_rect.collidepoint(mouse_pos):

                self.play = True
                self.load_map(0, 0)
                # import loading_screen


            elif instructions_rect.collidepoint(mouse_pos):
                print("instructions")

            elif quit_rect.collidepoint(mouse_pos):
                quit()

    def load_start_screen_img(self):

        self.start_background = pygame.image.load('../graphics/start_screen/Menu_Title.png').convert_alpha()
        self.play_button = pygame.image.load('../graphics/start_screen/Play.png').convert_alpha()
        self.quit_button = pygame.image.load('../graphics/start_screen/Quit.png').convert_alpha()
        self.instructions_button = pygame.image.load('../graphics/start_screen/Instructions.png').convert_alpha()
        self.loaded_img = True

    def load_map(self, map_code):
        # background here
        self.visible_sprites.set_map(map_code)
        map_objects = {
            'filler': load_csv_layout('../graphics/maps/' + str(map_code) + '/map_filler.csv'),
            'boundaries': load_csv_layout('../graphics/maps/' + str(map_code) + '/map_boundaries.csv'),
            'beings': load_csv_layout('../graphics/maps/' + str(map_code) + '/map_beings.csv'),
            'objects': load_csv_layout('../graphics/maps/' + str(map_code) + '/map_objects.csv')
        }
        images = {
            'filler': import_asset('../graphics/maps/' + str(map_code) + '/filler'),
            'objects': import_asset('../graphics/maps/' + str(map_code) + '/objects')
        }

        for object, graphic in map_objects.items():
            for row_index, row in enumerate(graphic):
                for col_index, col in enumerate(row):
                    if col != 'x':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE

                        if object == 'boundry':
                            Tile((x, y), [self.obstacle_sprites], 'invisible')

                        if object == 'filler':
                            random_filler_image = choice(images['filler'])
                            Tile((x, y), [self.visible_sprites], 'filler', random_filler_image)

                        if object == 'objects':
                            if col == 'c':
                                Tile((x, y), [self.visible_sprites, self.chest_sprites, self.obstacle_sprites], 'chest')
                                self.chests.append(Chest(x, y))

                            else:
                                surf = images['objects'][int(col)]
                                Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'objects', surf)

                        if object == 'beings':

                            if col == 'p':

                                self.player = Player(x, y, [self.visible_sprites], self.obstacle_sprites)
                            else:
                                self.enemies.append(
                                    Enemy(col, map_code, (x, y), [self.visible_sprites], self.obstacle_sprites))

        # passing the player and the chests list to the user action menu so they can be sued there
        self.user_action.set_chest_list(self.chests)
        self.user_action.set_player(self.player)
        self.user_action.set_enemies(self.enemies)

    def run(self):

        if not self.play:
            self.start_screen()

        else:

            self.visible_sprites.draw_all(self.player)
            self.visible_sprites.update()
            self.keys = pygame.key.get_pressed()
            self.user_action.key_pressed(self.keys)
            self.user_action.set_offset(self.visible_sprites.get_offset())

            if not self.user_action.get_loaded():
                self.user_action.set_loaded(True)


# this is for the adjusting of the screen how the camera follows it around
class Camera(pygame.sprite.Group):
    def __init__(self):
        # general setup
        super().__init__()
        self.battle = battle()
        self.Inventory = Inventory()

        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] / 2
        self.half_height = self.display_surface.get_size()[1] / 2
        self.offset = pygame.math.Vector2()
        



    def set_map(self, map):

        if map == 0:
            self.floor_surf = pygame.image.load('../graphics/maps/Map0.png').convert()
            self.floor_rect = self.floor_surf.get_rect(topleft=(576, 320))

        elif map == 1:
            print("2nd map here")
            self.floor_surf = pygame.image.load('../graphics/maps/Map1.png').convert()
            self.floor_rect = self.floor_surf.get_rect(topleft=(576, 320))

        else:
            print("3rd map here")

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

    def set_spell_info_status(self, status):
        global spell_info

        spell_info = status

    def set_equip_info_status(self, status):
        global equip_info

        equip_info = status

    # includes drawing inventory
    def draw_all(self, player):
        # getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        if not self.battle.get_battle_status():

            if inven_open:

                if item_info:

                    self.draw_sprites()
                    self.Inventory.draw_inven()
                    self.Inventory.draw_item_info()

                elif spell_info:
                    self.draw_sprites()
                    self.Inventory.draw_inven()
                    self.Inventory.draw_spell_info()

                elif equip_info:
                    self.draw_sprites()
                    self.Inventory.draw_inven()
                    self.Inventory.draw_equip_info()

                else:
                    self.draw_sprites()
                    self.Inventory.draw_inven()
            else:
                self.draw_sprites()
        else:
            self.battle.draw_battle()




    # draws map sprites only, no inventory stuff drawn here
    def draw_sprites(self):

        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
