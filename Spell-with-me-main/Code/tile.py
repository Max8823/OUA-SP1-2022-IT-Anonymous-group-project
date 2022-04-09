import pygame
from config import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type):

        super().__init__(groups)

        # add different sprite types here for specific sprites, trees, rocks, ect
        if sprite_type == 'boundry':
            self.image = pygame.image.load('../graphics/boundries/smiley.png').convert_alpha()
            self.rect = self.image.get_rect(center=pos)
            self.hitbox = self.rect.inflate(0, -10)

        if sprite_type == 'chest':
            self.image = pygame.image.load('../graphics/objects/chests/chest.png').convert_alpha()
            self.rect = self.image.get_rect(center=pos)
            self.hitbox = self.rect.inflate(-20, -20)

        if sprite_type == 'chest_e':
            self.image = pygame.image.load('../graphics/objects/chests/empty_chest.png').convert_alpha()
            self.rect = self.image.get_rect(center=pos)
            self.hitbox = self.rect.inflate(-20, -20)
