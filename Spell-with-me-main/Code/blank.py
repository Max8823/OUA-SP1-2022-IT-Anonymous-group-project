self.battle.end_battle()
                self.in_battle = False
                self.Inventory.add_item(self.battle.get_battle_loot()[0], self.battle.get_battle_loot()[1])
                self.set_items(self.Inventory.get_items_list())