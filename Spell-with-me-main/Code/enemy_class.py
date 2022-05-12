import pygame
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_code, map_code, pos, groups, obstacle_sprites):
        super().__init__(groups)

        self.enemy_level = 1
        self.qty = 0
        self.item_code = 0
        self.map_code = map_code
        self.enemy_code = int(enemy_code)
        self.map_code = map_code
        self.enemy_pos = pos

        ##################################################################################
        # need to change these values later once we have enemies done
        # atm each enemy would drop 2 items, add to dict to increase count,

        if self.enemy_code == 0:

            if map_code == 0:
                self.enemy_name = "frog"
                self.enemy_health = 150
                self.image = pygame.image.load('../graphics/enemies/frog.png').convert_alpha()
                self.rect = self.image.get_rect(center=self.enemy_pos)
                self.enemy_spells = {
                    "Acid spit": {"spell_id": 0, "damage": 100, "img": '..'},
                    "Lick": {"spell_id": 1, "damage": 100, "img": '..'},
                    "Roll": {"spell_id": 2, "damage": 150, "img": '..'},
                }
                self.enemy_loot = {"item_code": self.get_item_code(), "qty": self.get_qty(1, 3)}

            elif map_code == 1:
                self.enemy_name = "rat"
                self.enemy_health = 250
                self.image = pygame.image.load('../graphics/enemies/rat.png').convert_alpha()
                self.rect = self.image.get_rect(center=self.enemy_pos)
                self.enemy_spells = {
                    "Tail whip": {"spell_id": 0, "damage": 100, "img": '..'},
                    "Bite": {"spell_id": 1, "damage": 100, "img": '..'},
                    "Scratch": {"spell_id": 2, "damage": 150, "img": '..'},
                }
                self.enemy_loot = {"item_code": self.get_item_code(), "qty": self.get_qty(1, 3)}

            else:
                self.enemy_name = "bat"
                self.enemy_health = 350
                self.image = pygame.image.load('../graphics/enemies/Bat.png').convert_alpha()
                self.rect = self.image.get_rect(center=self.enemy_pos)
                self.enemy_spells = {
                    "Screech": {"spell_id": 0, "damage": 150, "img": '..'},
                    "Bite": {"spell_id": 1, "damage": 200, "img": '..'},
                    "Gust of wind": {"spell_id": 2, "damage": 250, "img": '..'},
                }

            self.enemy_loot = {"item_code": self.get_item_code(), "qty": self.get_qty(1, 3)}


        elif self.enemy_code == 1:
            if map_code == 0:
                self.enemy_name = "Wolf"
                self.enemy_health = 250
                self.image = pygame.image.load('../graphics/enemies/wolf.png').convert_alpha()
                self.rect = self.image.get_rect(center=self.enemy_pos)
                self.enemy_spells = {
                    "Scratch": {"spell_id": 0, "damage": 150, "img": '..'},
                    "Howl": {"spell_id": 1, "damage": 175, "img": '..'},
                    "Ferocious bite": {"spell_id": 2, "damage": 250, "img": '..'},
                }
                self.enemy_loot = {"item_code": self.get_item_code(), "qty": self.get_qty(1, 3)}

            elif map_code == 1:
                self.enemy_name = "Zombie"
                self.enemy_health = 350
                self.image = pygame.image.load('../graphics/enemies/zombie.png').convert_alpha()
                self.rect = self.image.get_rect(center=self.enemy_pos)
                self.enemy_spells = {
                    "Kick": {"spell_id": 0, "damage": 175, "img": '..'},
                    "Punch": {"spell_id": 1, "damage": 220, "img": '..'},
                    "Bite": {"spell_id": 2, "damage": 250, "img": '..'},
                }
                self.enemy_loot = {"item_code": self.get_item_code(), "qty": self.get_qty(1, 3)}

            else:
                self.enemy_name = "Ghost"
                self.enemy_health = 450
                self.image = pygame.image.load('../graphics/enemies/ghost.png').convert_alpha()
                self.rect = self.image.get_rect(center=self.enemy_pos)
                self.enemy_spells = {
                    "Haunt": {"spell_id": 0, "damage": 200, "img": '..'},
                    "pass through": {"spell_id": 1, "damage": 225, "img": '..'},
                    "Curse": {"spell_id": 2, "damage": 275, "img": '..'},
                }
                self.enemy_loot = {"item_code": self.get_item_code(), "qty": self.get_qty(1, 3)}


        elif self.enemy_code == 2:
            if map_code == 0:
                self.enemy_name = "Haunted Tree"
                self.enemy_health = 550
                self.image = pygame.image.load('../graphics/enemies/forest_boss.png').convert_alpha()
                self.rect = self.image.get_rect(center=self.enemy_pos)
                # add rect here later

                self.enemy_spells = {
                    "Inferno": {"spell_id": 0, "damage": 175, "img": '..'},
                    "Mind Control": {"spell_id": 1, "damage": 200, "img": '..'},
                    "Dark Mist": {"spell_id": 2, "damage": 300, "img": '..'},
                    "Terrify": {"spell_id": 3, "damage": 300, "img": '..'}
                }
                self.enemy_loot = {"item_code": self.get_item_code(), "qty": self.get_qty(1, 3)}

            elif map_code == 1:
                self.enemy_name = "grim reaper"
                self.enemy_health = 650
                self.image = pygame.image.load('../graphics/enemies/reaper_boss.png').convert_alpha()
                self.rect = self.image.get_rect(center=self.enemy_pos)
                # add rect here later

                self.enemy_spells = {
                    "Reap": {"spell_id": 0, "damage": 150, "img": '..'},
                    "Haunt": {"spell_id": 1, "damage": 200, "img": '..'},
                    "Cleave": {"spell_id": 2, "damage": 300, "img": '..'},
                    "Horrify": {"spell_id": 3, "damage": 350, "img": '..'}
                }
                self.enemy_loot = {"item_code": self.get_item_code(), "qty": self.get_qty(1, 3)}

            else:
                self.enemy_name = "Knight"
                self.enemy_health = 750
                self.image = pygame.image.load('../graphics/enemies/castle_boss.png').convert_alpha()
                self.rect = self.image.get_rect(center=self.enemy_pos)
                # add rect here later

                self.enemy_spells = {
                    "Inferno": {"spell_id": 0, "damage": 100, "img": '..'},
                    "Mind Control": {"spell_id": 1, "damage": 100, "img": '..'},
                    "Dark Mist": {"spell_id": 2, "damage": 300, "img": '..'},
                    "Terrify": {"spell_id": 3, "damage": 300, "img": '..'}
                }

                self.enemy_loot = {"item_code": self.get_item_code(), "qty": self.get_qty(1, 3)}

    def draw_enemy_health(self):
        if self.player_current_health < self.player_target_health:
            self.player_current_health += self.change_speed

        if self.player_current_health > self.player_target_health:
            self.player_current_health -= self.change_speed

        health_bar_width = int(self.player_current_health / self.health_ratio)
        health_bar = pygame.Rect(10, 45, health_bar_width, 25)
        pygame.draw.rect(pygame.display.get_surface(), (255, 0, 0), health_bar)


    def get_loot(self):


        if int(self.enemy_loot["item_code"]) in (4,5,6,7):

            loot = int(self.enemy_loot["item_code"]), 1
        else:
            loot = int(self.enemy_loot["item_code"]), int(self.enemy_loot["qty"])

        return loot


    def get_item_code(self):
        item_code = random.randrange(0, 9)
        return item_code

    def get_qty(self, r1, r2):
        qty = random.randrange(r1, r2)
        return qty

    def get_enemy_name(self):
        return self.enemy_name

    def get_enemy_health(self):
        return self.enemy_health

    def set_enemy_health(self, value):
        self.health = value

    def enemy_cast_spell(self, spell):
        return self.enemy_spells[spell]

    def get_enemy_image(self):
        return self.image

    def get_enemy_pos(self):
        return self.enemy_pos

    def set_enemy_pos(self):
        self.enemy_pos = (0,0)
