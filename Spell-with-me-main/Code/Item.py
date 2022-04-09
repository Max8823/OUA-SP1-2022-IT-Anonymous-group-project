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

            self.image = pygame.image.load('../graphics/items/small/green_potion.png').convert_alpha()
            self.rect = self.image.get_rect(center=(0, 0))
            self.image_large = pygame.image.load('../graphics/items/large/green_potion_large.png').convert_alpha()
            self.image_large.set_alpha(175)
            self.info = {"item_name": "ENERGY POTION", "descrip": "restores some energy", "equip": False,
                         "consume": True, "img": self.image_large}


        elif self.item_code == 2:

            self.image = pygame.image.load('../graphics/items/small/axe1.png').convert_alpha()
            self.rect = self.image.get_rect(center=(0, 0))
            self.image_large = pygame.image.load('../graphics/items/large/axe1_large.png').convert_alpha()
            self.image_large.set_alpha(175)
            self.info = {"item_name": "AXE", "descrip": "i could use this...", "equip": True, "consume": False,
                         "img": self.image_large}


        elif self.item_code == 3:

            self.image = pygame.image.load('../graphics/items/small/blue_potion.png').convert_alpha()
            self.rect = self.image.get_rect(center=(0, 0))
            self.image_large = pygame.image.load('../graphics/items/large/blue_potion_large.png').convert_alpha()
            self.image_large.set_alpha(175)
            self.info = {"item_name": "MANA POTION", "descrip": "restores some mana", "equip": False, "consume": True,
                         "img": self.image_large}


        elif self.item_code == 4:

            self.image = pygame.image.load('../graphics/items/small/book1.png').convert_alpha()
            self.rect = self.image.get_rect(center=(0, 0))
            self.image_large = pygame.image.load('../graphics/items/large/book1_large.png').convert_alpha()
            self.image_large.set_alpha(175)
            self.info = {"item_name": "LIGHTNING BOLT", "descrip": "consume to learn lightning bolt", "equip": False,
                         "consume": True, "img": self.image_large}


        elif self.item_code == 5:

            self.image = pygame.image.load('../graphics/items/small/book2.png').convert_alpha()
            self.rect = self.image.get_rect(center=(0, 0))
            self.image_large = pygame.image.load('../graphics/items/large/book2_large.png').convert_alpha()
            self.image_large.set_alpha(175)
            self.info = {"item_name": "ICE BLAST", "descrip": "consume to learn iceblast ", "equip": False,
                         "consume": True, "img": self.image_large}


        elif self.item_code == 6:

            self.image = pygame.image.load('../graphics/items/small/book3.png').convert_alpha()
            self.rect = self.image.get_rect(center=(0, 0))
            self.image_large = pygame.image.load('../graphics/items/large/book3_large.png').convert_alpha()
            self.image_large.set_alpha(175)
            self.info = {"item_name": "FIRE BALL", "descrip": "consume to learn fireball ", "equip": False,
                         "consume": True, "img": self.image_large}


        elif self.item_code == 7:

            self.image = pygame.image.load('../graphics/items/small/sword1.png').convert_alpha()
            self.rect = self.image.get_rect(center=(0, 0))
            self.image_large = pygame.image.load('../graphics/items/large/sword1_large.png').convert_alpha()
            self.image_large.set_alpha(175)
            self.info = {"item_name": "SWORD", "descrip": "its very sharp!", "equip": True, "consume": False,
                         "img": self.image_large}


        else:
            self.item_code = 8
            self.image = pygame.image.load('../graphics/items/small/heart.png').convert_alpha()
            self.rect = self.image.get_rect(center=(0, 0))
            self.image_large = pygame.image.load('../graphics/items/large/heart_large.png').convert_alpha()
            self.image_large.set_alpha(175)
            self.info = {"item_name": "HEALTH BOOST", "descrip": "Consume to increase maximum health \n by 1",
                         "equip": False, "consume": True, "img": self.image_large}

    def get_item_info(self):
        return self.info

    def get_item_img(self):
        return self.image

    def get_item_code(self):
        print(self.item_code)
        return self.item_code

    def set_item_code(self, item_code):
        self.item_code = item_code

    def increase_item_count(self, qty):
        print("increased")
        self.item_count += qty

    def decrease_item_count(self,qty):
        self.item_count += qty

    def get_item_count(self):
        return self.item_count

    def get_item_pos(self):
        return self.pos

    def set_item_pos(self, pos):
        self.pos = pos
