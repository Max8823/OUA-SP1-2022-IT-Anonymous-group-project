import threading
import time

import pygame
from os import walk


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, groups, obstacle_sprites):
        super().__init__(groups)

        self.image = pygame.image.load('../graphics/player/down/down0.png').convert_alpha()

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

        self.load_player_animations()

        self.player_spells = {
            "Fire Blast": {"spell_id": 0,"damage": 100, "learnt": True, "img": '..'},
            "Water Blast": {"spell_id": 1,"damage": 100, "learnt": True, "img": '..'},
            "Earth Blast": {"spell_id": 2,"damage": 100, "learnt": True, "img": '..'},
            "Air Blast": {"spell_id": 3,"damage": 100, "learnt": True, "img": '..'},
            "Fire Fury": {"spell_id": 4,"damage": 300, "learnt": False, "img": '..'},
            "Water Fury": {"spell_id": 5,"damage": 300, "learnt": False, "img": '..'},
            "Earth Fury": {"spell_id": 6,"damage": 300, "learnt": False, "img": '..'},
            "Air Fury": {"spell_id": 7,"damage": 300, "learnt": False, "img": '..'},
        }
        ##
        self.player_current_health = 300
        self.player_max_health = 1000
        self.health_bar_length = 400
        self.target_health = 500
        self.health_ratio = self.player_max_health / self.health_bar_length
        self.change_speed = 1

    def draw_player_health(self):
        transition_width = 0
        transition_color = (255, 0, 0)

        if self.player_current_health < self.target_health:
            self.player_current_health += self.change_speed
            transition_width = int((self.target_health - self.player_current_health) / self.health_ratio)
            transition_color = (0, 255, 0)

        if self.player_current_health > self.target_health:
            self.player_current_health -= self.change_speed
            transition_width = int((self.target_health - self.player_current_health) / self.health_ratio)
            transition_color = (255, 255, 0)

        health_bar_width = int(self.player_current_health / self.health_ratio)
        health_bar = pygame.Rect(10, 45, health_bar_width, 25)
        new_bar = pygame.Rect(health_bar.right, 45, transition_width, 25)

        pygame.draw.rect(pygame.display.get_surface(), (255, 0, 0), health_bar)
        pygame.draw.rect(pygame.display.get_surface(), transition_color, new_bar)


    def set_player_health(self, damage):
        self.player_current_health -= damage

    def heal_player(self, healing):
        self.player_current_health += healing

    def load_player_animations(self):
        animation_path = '../graphics/player/'
        self.player_animations = {'down': [], 'left': [], 'right': [], 'up': [], 'down_standing': [],
                                  'left_standing': [], 'right_standing': [], 'up_standing': []}

        for animation in self.player_animations.keys():
            img_path = animation_path + animation
            self.player_animations[animation] = self.load_animations(img_path)

    def animate(self):

        animation = self.player_animations[self.facing]
        self.frame_index += self.animation_speed

        if self.frame_index >= len(animation):
            self.frame_index = 0
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center=self.hitbox.center)

    def load_animations(self, path):

        animations = []
        for _, __, img_files in walk(path):
            for image in img_files:
                full_path = path + '/' + image

                next_animation = pygame.image.load(full_path).convert_alpha()

                animations.append(next_animation)

        return animations

    def set_player_facing(self, facing):

        self.facing = facing

    def get_player_facing(self):
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'standing' in self.facing and not self.inBattle:
                self.facing = self.facing + '_standing'

    def get_spell(self):
        return self.player_spells

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
    def update(self):
        self.get_player_facing()
        self.animate()
        self.draw_player_health()
