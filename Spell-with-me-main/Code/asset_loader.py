from csv import reader
from os import walk
import pygame


def load_csv_layout(path):
    map_objects = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter=',')
        for row in layout:
            map_objects.append(list(row))
        return map_objects


def import_asset(path):
    asset_list = []

    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_local = pygame.image.load(full_path).convert_alpha()
            asset_list.append(image_local)

    return asset_list
