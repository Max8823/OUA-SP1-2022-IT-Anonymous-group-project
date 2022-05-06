import pygame


class Portal:

    def __init__(self, pos, map_code):

        self.pos = pos
        self.map_code = map_code

    def get_position(self):

        return self.pos