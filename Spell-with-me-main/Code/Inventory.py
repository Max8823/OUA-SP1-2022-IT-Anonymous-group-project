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
spell_background = pygame.image.load('../graphics/inventory/Spell_box.png')


# ITEM DISPLAY
target_item = 0
target_spell = "None"
slot_counter = 0

items_list = []
equipped_items = []
spells = {}
spells_pos = []



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
        self.spell_display_up = False

##############

    # creatiing the inventory
    def draw_inven(self):

        self.screen.blit(inven_background, (200, 100))

        self.slot_x = 635
        self.slot_y = 100
        self.item_posX = 640
        self.item_posY = 105

        i = 0
        for rows in range(self.rows):

            self.slot_x = 635
            self.slot_y += 80

            self.item_posX = 640
            self.item_posY += 80


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
                    self.item_posX += 116
                    self.slot_x += 116

                    i += 1

                else:
                    self.screen.blit(item_slot, (self.slot_x, self.slot_y))

                    self.slot_x += 116

        self.draw_equipment()
        self.draw_spells()


    def set_spells(self, player_spells):
        global spells

        spells = player_spells.copy()

    def draw_spells(self):
        global spells

        spell_slotx = 282
        spell_sloty = 218


#Fire spells
        self.screen.blit(spell_background, (spell_slotx, spell_sloty))
        self.screen.blit(spells['Fire Blast']['img'], (spell_slotx+20, spell_sloty+15))
        fire_blast_rect = spell_slotx+20, spell_sloty+15
        self.set_spell_pos((fire_blast_rect, "Fire Blast"))



        self.screen.blit(spell_background, (spell_slotx-64, spell_sloty+64))
        if spells['Fire Fury']['learnt']:
            self.screen.blit(spells['Fire Fury']['img'], (spell_slotx -44, spell_sloty + 79))
            fire_fury_rect = spell_slotx-44, spell_sloty+79
            self.set_spell_pos((fire_fury_rect, "Fire Fury"))



#Water spells
        self.screen.blit(spell_background, (spell_slotx + 118, spell_sloty))
        self.screen.blit(spells['Water Blast']['img'], (spell_slotx + 138, spell_sloty+15))
        water_blast_rect = spell_slotx+138, spell_sloty+15
        self.set_spell_pos((water_blast_rect, "Water Blast"))


        self.screen.blit(spell_background, (spell_slotx + 188, spell_sloty +64))
        if spells['Water Fury']['learnt']:
            self.screen.blit(spells['Water Fury']['img'], (spell_slotx + 208, spell_sloty + 79))
            water_fury_rect = spell_slotx+208, spell_sloty+79
            self.set_spell_pos((water_fury_rect, "Water Fury"))


#air spells
        self.screen.blit(spell_background, (spell_slotx+118, spell_sloty+256))
        self.screen.blit(spells['Air Blast']['img'], (spell_slotx + 138, spell_sloty +276))
        air_blast_rect = spell_slotx+138, spell_sloty+276
        self.set_spell_pos((air_blast_rect, "Air Blast"))


        self.screen.blit(spell_background, (spell_slotx+ 188, spell_sloty + 192))
        if spells['Air Fury']['learnt']:
            self.screen.blit(spells['Air Fury']['img'], (spell_slotx + 208, spell_sloty + 212))
            Air_Fury_rect = (spell_slotx+208, spell_sloty+212)
            self.set_spell_pos((Air_Fury_rect, "Air Fury"))


#Earth spells
        self.screen.blit(spell_background, (spell_slotx, spell_sloty+256))
        self.screen.blit(spells['Earth Blast']['img'], (spell_slotx +20, spell_sloty + 276))
        earth_blast_rect = spell_slotx+20, spell_sloty+276
        self.set_spell_pos((earth_blast_rect, "Earth Blast"))


        self.screen.blit(spell_background, (spell_slotx -64 , spell_sloty +192))
        if spells['Earth Fury']['learnt']:
            self.screen.blit(spells['Earth Fury']['img'], (spell_slotx -44, spell_sloty+ 212))
            earth_fury_rect = spell_slotx-44, spell_sloty+212
            self.set_spell_pos((earth_fury_rect, "Earth Blast"))




    def draw_equipment(self):
        global equipped_items

        for item in equipped_items:
            print("do work here")


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
        item_header_text_rect = item_header_text.get_rect()
        item_header_text_rect.center = (self.screen.get_width() // 2, 75)


    def equip_item(self, target_item):
        global equipped_items

        if len(equipped_items) <= 3:
            equipped_items.append(target_item)
            items_list[target_item].pop()

        else:
            print("all equipment slots full")



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

    def set_taregt_spell(self, target):
        global target_spell
        target_spell = target

    def get_target_spell(self):
        global  target_spell
        return target_spell

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

    def set_spell_display_up(self, status):
        self.spell_display_up = status

    def get_spell_display_up(self):
        return  self.spell_display_up

    def set_spell_pos(self, spell):
        global spells_pos

        if len(spells_pos) < 8:
            if spell not in spells_pos:
                spells_pos.append(spell)


    def get_spell_pos(self):
        global spells_pos

        return spells_pos


    def draw_spell_info(self):
        global target_spell

        spell_name = target_spell
        spell_header_text = item_header.render(spell_name, False, (255,0,0))

        spell_descrip = 'damage : ' + str(spells[target_spell]["damage"])
        spell_descrip_text = item_description.render(spell_descrip, False,(0,0,0))

        # background for the item information
        item_background_rect = self.item_background.get_rect()
        # this will make the item info background appear in the center of the screen
        item_background_rect.center = (self.screen.get_width() // 2, self.screen.get_height() // 2)
        self.screen.blit(self.item_background, item_background_rect)

        spell_header_text_rect = spell_header_text.get_rect()
        spell_header_text_rect.center = (item_background_rect.center[0], item_background_rect.center[1] - 300)
        self.screen.blit(spell_header_text, spell_header_text_rect)
        pygame.draw.line(self.screen, (255, 0, 0), (spell_header_text_rect[0], spell_header_text_rect.center[1] + 50),
                         (spell_header_text_rect.right, spell_header_text_rect.center[1] + 50), 3)

        item_descrip_rect = spell_descrip_text.get_rect()
        item_descrip_rect.center = (item_background_rect.center[0], item_background_rect.center[1] + 100)
        self.screen.blit(spell_descrip_text, item_descrip_rect)



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