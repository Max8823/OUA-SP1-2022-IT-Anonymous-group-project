import threading
import time

import pygame
from os import walk


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, groups, obstacle_sprites):
        super().__init__(groups)

        self.image = pygame.image.load('../graphics/player/player_down.png').convert_alpha()

        # do not change
        self.rect = self.image.get_rect(center=(x, y))

        # hitbox can put player infromt/behind sprites, deals with collisions
        self.hitbox = self.rect.inflate(0, -25)

        self.direction = pygame.math.Vector2()
        self.speed = 4
        self.obstacle_sprites = obstacle_sprites

        # marks what sprite in animation is being used and how quick they will change
        self.frame_index = 0
        self.animation_speed = 0.10

        # used to change what animation / sprite is used for what direction the player is facing
        self.facing = 'down'

        # will be used when starting battle
        self.inBattle = False

        self.player_health = 3



    def get_player_pos(self):
        self.pos = self.rect.centerx, self.rect.centery
        return self.pos

    def set_player_facing(self, facing):
        self.facing = facing

    def set_player_direction_y(self, direction_y):
        self.direction.y = direction_y

    def set_player_direction_x(self, direction_x):
        self.direction.x = direction_x

    def get_player_rect(self):
        return self.rect

    def normalise_player_direction_y(self, coll_type):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
            self.hitbox.y += self.direction.y * self.speed
            self.collision(coll_type)
            self.rect.center = self.hitbox.center

    def normalise_player_direction_x(self, coll_type):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
            self.hitbox.x += self.direction.x * self.speed
            self.collision(coll_type)
            self.rect.center = self.hitbox.center

    # used for colliding with sprites / walls, trees, ect
    def collision(self, direction):

        # outer if statement for moving horizontally
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    # used if moving right to mark collision
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left

                    # used if moving left to mark collision
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right

        # outer if statement for vertical movements
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    # used if moving down to mark collision
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top

                    # used if moving up to mark collision
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom

    # updating user input


