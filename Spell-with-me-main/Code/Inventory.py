import pygame

from Item import Item
import config

pygame.init()

pygame.font.init()
# FONTS
font = pygame.freetype.Font(pygame.font.match_font("calibiri"), 26)
item_header = pygame.font.Font('../fonts/Tangerine-Bold.ttf', 50)
item_description = pygame.font.Font('../fonts/Tangerine-Bold.ttf', 45)

# INVENTORY BACKGROUND
inven_background = pygame.image.load('../graphics/inventory/inven_background.png')
item_slot = pygame.image.load('../graphics/inventory/item_slot.png')

# ITEM DISPLAY
target_item = 0
slot_counter = 0
items_list = []


class Inventory:
    def __init__(self):

        self.item = Item

        # number of rows, columns in the inventory
        self.rows = 3
        self.col = 3

        # following dimensions are for building and displaying the inventory and items slots
        self.slot_x = 64
        self.slot_y = 64
        self.border = 3
        self.slot_counter = 1

        # target item used to bring up additional item info
        self.target_item = 0

        self.screen = pygame.display.get_surface()
        self.load_img()
        self.inventory_full = False
        self.item_display_up = False

##############

    def draw_spells(self):
        ##################
        print("no")


    # creatiing the inventory
    def draw_inven(self):

        global slot_counter

        self.screen.blit(inven_background, (200, 100))

        self.slot_x = 750
        self.slot_y = 100
        self.item_posX = 755
        self.item_posY = 105

        i = 0
        for rows in range(self.rows):
            self.slot_x = 750
            self.slot_y += 68
            self.item_posX = 755
            self.item_posY += 68

            for col in range(self.col):

                if slot_counter > i:

                    # displaying the inventory slot and the image that will be inside
                    self.screen.blit(item_slot, (self.slot_x, self.slot_y))
                    self.screen.blit(items_list[i].get_item_img(), (self.item_posX, self.item_posY))
                    items_list[i].set_item_pos((self.item_posX, self.item_posY))

                    # displaying the counter or quantity or any given item
                    qty = items_list[i].get_item_count()
                    text_surface, rect = font.render(str(qty), (0, 0, 0))
                    self.screen.blit(text_surface, (self.item_posX + 5, self.item_posY + 5))
                    self.item_posX += 68
                    self.slot_x += 68

                    i += 1

                else:
                    self.screen.blit(item_slot, (self.slot_x, self.slot_y))
                    self.slot_x += 68

    def add_item(self, item_code, qty):
        global slot_counter
        pos = (0, 0)
        match = False
        # if items_list is empty( if user has not picked anything up yet)

        if not items_list:
            item = Item(item_code, qty, pos)
            items_list.append(item)
            slot_counter += 1
        else:
            i = 0

            for items in items_list:
                if items.get_item_code() is item_code:
                    items.increase_item_count(qty)
                    i += 1
                    match = True
                else:
                    i += 1

            if self.slot_counter <= 8 and match is False:
                item = Item(item_code, qty, pos)
                items_list.append(item)
                slot_counter += 1

            else:
                if slot_counter == 8:
                    print("inventory is full")

    def full_inventory(self):

        item_header_text = item_header.render("the inventory is full", False, (0, 0, 0))
        print(item_header_text)
        item_header_text_rect = item_header_text.get_rect()
        item_header_text_rect.center = (self.screen.get_width() // 2, 75)

    def get_items_list(self):
        return items_list

    def get_inventory_full(self):
        return self.inventory_full

    def set_target_item(self, target):
        global target_item

        target_item = target

    def get_target_item(self):
        global target_item

        return target_item

    def consume_item(self):
        global slot_counter, target_item

        items_list[target_item].decrease_item_count(1)

        if items_list[target_item].get_item_count() == 0:
            items_list.pop(target_item)
            slot_counter -= 1
            target_item = None
            self.set_target_item(None)
            self.set_item_display_up(False)

    def get_item_display_up(self):
        return self.item_display_up

    def set_item_display_up(self, status):
        self.item_display_up = status


    # change the + and - values to change their positioning when real graphics come in
    # drawing the additional item info screen
    def draw_item_info(self):
        global target_item
        i = target_item

        if items_list:

            if i is not None:

                item_name = items_list[i].get_item_info()["item_name"]
                item_header_text = item_header.render(item_name, False, (255, 0, 0))

                item_descrip = items_list[i].get_item_info()["descrip"]
                item_descrip_text = item_description.render(item_descrip, False, (0, 0, 0))

                # background for the item information
                item_background_rect = self.item_background.get_rect()
                # this will make the item info background appear in the center of the screen
                item_background_rect.center = (self.screen.get_width() // 2, self.screen.get_height() // 2)
                self.screen.blit(self.item_background, item_background_rect)

                # item name + line below
                item_header_text_rect = item_header_text.get_rect()
                item_header_text_rect.center = (item_background_rect.center[0], item_background_rect.center[1] - 300)
                self.screen.blit(item_header_text, item_header_text_rect)
                pygame.draw.line(self.screen, (255, 0, 0), (item_header_text_rect[0], item_header_text_rect.center[1] + 50),
                                 (item_header_text_rect.right, item_header_text_rect.center[1] + 50), 3)

                # item image + line below
                item_image_rect = items_list[i].get_item_info()["img"].get_rect()
                item_image_rect.center = (item_background_rect.center[0], item_background_rect.center[1] - 100)
                self.screen.blit(items_list[i].get_item_info()["img"], item_image_rect)
                pygame.draw.line(self.screen, (255, 0, 0), (item_header_text_rect[0], item_image_rect.center[1] + 150),
                                 (item_header_text_rect.right, item_image_rect.center[1] + 150), 3)

                # description text
                item_descrip_rect = item_descrip_text.get_rect()
                item_descrip_rect.center = (item_background_rect.center[0], item_background_rect.center[1] + 100)
                self.screen.blit(item_descrip_text, item_descrip_rect)

                # setting cancel button, which will close the pop-up
                item_display_cancel_rect = self.item_display_cancel.get_rect()
                item_display_cancel_rect.center = (item_background_rect.center[0] - 150, item_background_rect.center[1] + 200)
                self.screen.blit(self.item_display_cancel, item_display_cancel_rect)
                # setting cancel pos
                self.set_display_cancel(item_display_cancel_rect)

                # if equippable / if not changes the buttons accordingly
                if items_list[i].get_item_info()["equip"]:
                    item_display_equip_rect = self.item_display_equip.get_rect()
                    item_display_equip_rect.center = (
                        item_background_rect.center[0] + 150, item_background_rect.center[1] + 200)
                    self.screen.blit(self.item_display_equip, item_display_equip_rect)
                    # setting equip item pos
                    self.set_display_equip_pos(item_display_equip_rect)
                    self.set_second_button(1)

                # if not equippable, display 'use item'
                else:
                    item_display_use_item_rect = self.item_display_use_item.get_rect()
                    item_display_use_item_rect.center = (
                        item_background_rect.center[0] + 150, item_background_rect.center[1] + 200)
                    self.screen.blit(self.item_display_use_item, item_display_use_item_rect)
                    # setting use item pos
                    self.set_display_use_item_pos(item_display_use_item_rect)
                    self.set_second_button(2)

            # following getters and setters are used / called when clicking on the item display 'icons'

    def set_second_button(self, type):
        self.type = type

    def get_second_button(self):
        return self.type

    def set_display_cancel(self, cancel_pos):
        self.cancel_pos = cancel_pos

    def get_cancel_pos(self):
        return self.cancel_pos

    def set_display_equip_pos(self, equip_pos):
        self.equip_pos = equip_pos

    def get_display_equip_pos(self):
        return self.equip_pos

    def set_display_use_item_pos(self, use_item_pos):
        self.use_item_pos = use_item_pos

    def get_display_use_item_pos(self):
        return self.use_item_pos

    # change set_alpha to higher number / 255 to reduce transparency, decrease to reduce
    def load_img(self):
        self.item_background = pygame.image.load('../graphics/inventory/item_display.png').convert_alpha()
        self.item_background.set_alpha(225)

        self.item_display_cancel = pygame.image.load('../graphics/inventory/item_display_cancel.png').convert_alpha()
        self.item_display_cancel.set_alpha(225)

        self.item_display_equip = pygame.image.load('../graphics/inventory/item_display_equip.png').convert_alpha()
        self.item_display_equip.set_alpha(225)

        self.item_display_use_item = pygame.image.load(
            '../graphics/inventory/item_display_use_item.png').convert_alpha()
        self.item_display_use_item.set_alpha(225)


        #