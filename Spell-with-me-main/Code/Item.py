import pygame


class Item:
    def __init__(self, item_code, qty, pos):

        self.set_item_code(item_code)
        self.item_count = qty
        self.pos = pos

        if self.item_code == 0:

            self.image = pygame.image.load('../graphics/items/small/hp_potion.png').convert_alpha()
            self.rect = self.image.get_rect(center=(0, 0))
            self.image_large = pygame.image.load('../graphics/items/large/hp_potion_large.png').convert_alpha()
            self.image_large.set_alpha(175)
            self.info = {"item_name": "HEALTH POTION", "descrip": "restores some health", "equip": False,
                         "consume": True, "img": self.image_large}


        elif self.item_code == 1:

            self.image = pygame.image.load('../graphics/items/small/ring.png').convert_alpha()
            self.rect = self.image.get_rect(center=(0, 0))
            self.image_large = pygame.image.load('../graphics/items/large/ring_large.png').convert_alpha()
            self.image_large.set_alpha(175)
            self.info = {"item_name": "Blue crystal ring", "descrip": "you feel stronger holding this in your hands...", "equip": True,
                         "consume": False, "img": self.image_large, "magic_pwr": 0.25}


        elif self.item_code == 2:

            self.image = pygame.image.load('../graphics/items/small/staff.png').convert_alpha()
            self.rect = self.image.get_rect(center=(0, 0))
            self.image_large = pygame.image.load('../graphics/items/large/staff_large.png').convert_alpha()
            self.image_large.set_alpha(175)
            self.info = {"item_name": "Forest staff", "descrip": "This weapon holds the power of the forest", "equip": True, "consume": False,
                         "img": self.image_large, "magic_pwr": 0.25}


        elif self.item_code == 3:

            self.image = pygame.image.load('../graphics/items/small/necklace.png').convert_alpha()
            self.rect = self.image.get_rect(center=(0, 0))
            self.image_large = pygame.image.load('../graphics/items/large/necklace_large.png').convert_alpha()
            self.image_large.set_alpha(175)
            self.info = {"item_name": "Castle guards necklace", "descrip": "a castle guards necklace", "equip": True, "consume": False,
                         "img": self.image_large, "magic_pwr": 0.25}


        elif self.item_code == 4:

            self.image = pygame.image.load('../graphics/items/small/book1.png').convert_alpha()
            self.rect = self.image.get_rect(center=(0, 0))
            self.image_large = pygame.image.load('../graphics/items/large/book1_large.png').convert_alpha()
            self.image_large.set_alpha(175)
            self.info = {"item_name": "Fire Fury", "descrip": "consume to learn Fire Fury", "equip": False,
                         "consume": True, "img": self.image_large}


        elif self.item_code == 5:

            self.image = pygame.image.load('../graphics/items/small/book2.png').convert_alpha()
            self.rect = self.image.get_rect(center=(0, 0))
            self.image_large = pygame.image.load('../graphics/items/large/book2_large.png').convert_alpha()
            self.image_large.set_alpha(175)
            self.info = {"item_name": "Water Fury", "descrip": "consume to learn Water Fury ", "equip": False,
                         "consume": True, "img": self.image_large}


        elif self.item_code == 6:

            self.image = pygame.image.load('../graphics/items/small/book3.png').convert_alpha()
            self.rect = self.image.get_rect(center=(0, 0))
            self.image_large = pygame.image.load('../graphics/items/large/book3_large.png').convert_alpha()
            self.image_large.set_alpha(175)
            self.info = {"item_name": "Earth Fury", "descrip": "consume to learn Earth Fury ", "equip": False,
                         "consume": True, "img": self.image_large}

        # previously known as sword, changed equip to false and consume to true
        # also updated description.
        elif self.item_code == 7:

            self.image = pygame.image.load('../graphics/items/small/book4.png').convert_alpha()
            self.rect = self.image.get_rect(center=(0, 0))
            self.image_large = pygame.image.load('../graphics/items/large/book4_large.png').convert_alpha()
            self.image_large.set_alpha(175)
            self.info = {"item_name": "Air Fury", "descrip": "consume to learn Air Fury", "equip": False, "consume": True,
                         "img": self.image_large}


        else:
            self.item_code = 8
            self.image = pygame.image.load('../graphics/items/small/heart.png').convert_alpha()
            self.rect = self.image.get_rect(center=(0, 0))
            self.image_large = pygame.image.load('../graphics/items/large/heart_large.png').convert_alpha()
            self.image_large.set_alpha(175)
            self.info = {"item_name": "HEALTH BOOST", "descrip": "Consume to increase maximum health by 100 \n by 1",
                         "equip": False, "consume": True, "img": self.image_large}

    def get_item_info(self):
        return self.info

    def get_item_img(self):
        return self.image

    def get_item_code(self):

        return self.item_code

    def set_item_code(self, item_code):
        self.item_code = item_code

    def increase_item_count(self, qty):
        self.item_count += qty

    def decrease_item_count(self,qty):
        self.item_count -= qty

    def get_item_count(self):
        return self.item_count

    def get_mag_pwr(self):
        return self.info["magic_pwr"]

    def get_item_name(self):
        return self.info["item_name"]


    def get_item_pos(self):
        return self.pos

    def set_item_pos(self, pos):
        self.pos = pos

    def get_item_rect(self):
        return self.rect