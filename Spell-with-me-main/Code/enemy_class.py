import pygame
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_code, groups, obstacle_sprites):
        super().__init__(groups)

        self.enemy_level = 1
        self.qty =0
        self.item_code =0

        ##################################################################################
        # need to change these values later once we have enemies done
        #atm each enemy would drop 2 items, add to dict to increase count,



        if enemy_code == 0:
            self.enemy_name = "enemy5"
            self.enemy_health = 4
            self.enemy_img = '..path to img'
            # add rect here later

            self.enemy_spells = {
                "Inferno": {"spell_id": 0, "damage": 100, "img": '..'},
                "Mind Control": {"spell_id": 1, "damage": 300, "img": '..'},
                "Dark Mist": {"spell_id": 2, "damage": 300, "img": '..'},
                "Terrify": {"spell_id": 3, "damage": 300, "img": '..'}
            }

            self.enemy_loot = {"item_code": self.get_item_code(),  "qty": self.get_qty(0, 2),
                               "item_code": 0, "qty": 1}



        elif enemy_code == 1:
            self.enemy_name = "enemy5"
            self.enemy_health = 4
            self.enemy_img = '..path to img'
            # add rect here later

            self.enemy_spells = {
                "Inferno": {"spell_id": 0, "damage": 100, "img": '..'},
                "Mind Control": {"spell_id": 1, "damage": 300, "img": '..'},
                "Dark Mist": {"spell_id": 2, "damage": 300, "img": '..'},
                "Terrify": {"spell_id": 3, "damage": 300, "img": '..'}
            }
            self.enemy_loot = {"item_code": self.get_item_code(), "qty": self.get_qty(0, 2),
                               "item_code": 0, "qty": 1}

        elif enemy_code == 2:
            self.enemy_name = "enemy5"
            self.enemy_health = 4
            self.enemy_img = '..path to img'
            # add rect here later

            self.enemy_spells = {
                "Inferno": 1,
                "Mind Control": 2,
                "Dark Mist": 2,
                "Terrify": 2
            }
            self.enemy_loot = {"item_code": self.get_item_code(), "qty": self.get_qty(0, 2),
                               "item_code": 0, "qty": 1}

        elif enemy_code == 4:
            self.enemy_name = "enemy5"
            self.enemy_health = 4
            self.enemy_img = '..path to img'
            # add rect here later

            self.enemy_spells = {
                "Inferno": {"spell_id": 0, "damage": 100, "img": '..'},
                "Mind Control": {"spell_id": 1, "damage": 300, "img": '..'},
                "Dark Mist": {"spell_id": 2, "damage": 300, "img": '..'},
                "Terrify": {"spell_id": 3, "damage": 300, "img": '..'}
            }

            self.enemy_loot = {"item_code": self.get_item_code(), "qty": self.get_qty(0, 2),
                               "item_code": 0, "qty": 1}

        else:
            self.enemy_name = "enemy5"
            self.enemy_health = 4
            self.enemy_img = '..path to img'
            # add rect here later

            self.enemy_spells = {
                "Inferno": {"spell_id": 0, "damage": 100, "img": '..'},
                "Mind Control": {"spell_id": 1, "damage": 300, "img": '..'},
                "Dark Mist": {"spell_id": 2, "damage": 300, "img": '..'},
                "Terrify": {"spell_id": 3, "damage": 300, "img": '..'}
            }

            self.enemy_loot = {"item_code": self.get_item_code(), "qty": self.get_qty(0, 2),
                               "item_code": 0, "qty": 1}

    def get_item_code(self):
        item_code = random.randrange(0, 9)
        return item_code

    def get_qty(self, r1, r2):
        qty = random.randrange(r1, r2)
        return qty

    def get_enemy_name(self):
        return self.enemy_name

    def get_enemy_health(self):
        return self.health

    def set_enemy_health(self, value):
        self.health = value

    def enemy_cast_spell(self, spell):

        return self.enemy_spells[spell]
