import pygame
from config import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, surface=pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        y_offset = HITBOX_OFFSET[sprite_type]
        self.image = surface

        if sprite_type == 'object':
            self.rect = self.image.get_rect(center=(pos[0], pos[1] + TILESIZE))
            self.hitbox = self.rect.inflate(50, y_offset)

        elif sprite_type == 'filler':
            self.rect = self.image.get_rect(center=pos)
            self.hitbox = self.rect.inflate(0, y_offset)

        elif sprite_type == 'chest':
            #this will always be 'top left'
            self.image = pygame.image.load('../graphics/objects/chests/chest.png').convert_alpha()
            self.rect = self.image.get_rect(center=pos)
            self.hitbox = self.rect.inflate(-20, -20)

        else:
            self.rect = self.image.get_rect(topleft=pos)
            self.hitbox = self.rect.inflate(0, y_offset)

    def get_sprite_type(self):
        return self.sprite_type
