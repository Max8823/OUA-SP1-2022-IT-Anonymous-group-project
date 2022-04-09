pygame.draw.rect(self.screen)
self.screen.blit(item_background, (300, 25))
item_name = items_list[i].get_item_info()["item_name"]
text_surface = item_header.render(item_name, False, (255, 0, 0))
self.screen.blit(text_surface, (400, 50))

self.screen.blit(items_list[i].get_item_info()["img"], (300, 200))