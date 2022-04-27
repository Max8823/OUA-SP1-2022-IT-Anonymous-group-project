import pygame
import random


class Chest:

    def __init__(self, x, y):
        self.posX = x
        self.posY = y
        self.contents = self.generate_contents()

    def get_chest_posX(self):
        return self.posX

    def get_chest_posY(self):
        return self.posY

    def get_chest_pos(self):
        self.pos = self.posX, self.posY
        return self.pos

    def get_chest_contents(self):
        return self.contents

    # this is temporary
    def generate_contents(self):
        item_code = random.randrange(0, 9)

        if item_code in {4,5,6,7}:
            qty = 1
        else:
            qty = random.randrange(1,5)

        return item_code, qty
