import pygame
import Inventory
import player
import enemy_class
import level
import config


class battle:
@@ -10,24 +12,52 @@
        self.inventory_open = False
        self.enemy = enemy
        self.player = player
        self.screen = pygame.display.get_surface()
    def set_battle(self, player, enemy):
        self.enemy = enemy
        self.player = player
    def get_battle_players(self):
        return self.enemy, self.player
    def draw_arena(self):
        self.screen.fill('white')
        self.get_battle_players()
        self.player = self.get_battle_players()[1]
        self.enemy = self.get_battle_players()[0]
        print(self.player.get_player_pos())

        print(self.player, self.enemy)

question_list = ["Is the word 'whistel' spelt correctly?", "Is the word 'knife' spelt correctly?",
                 "Is the word 'wriggle' spelt correctly?", "Is the word 'rong' spelt correctly?",
                 "Does a 'night' wear armour?", "Does a 'which' cast spells?", "Does 'their' describe something "
                 "belonging to a person?", "What does an archer shoot out of his bow?", "What is white, scary, and "
                 "says 'boo' at night?", "What is the main city of Victoria?", "What is the main city of South "
                 "Australia?", "Is the word 'knowlege' spelt correctly?", "Is 'where' a location word?", "What word do you "
                 "live in and rhymes with 'mouse'?", "What is the opposite of 'noisy' and rhymes with 'diet'?", "What "
                 "do you use to buy things with?", "I help you to learn in class, what am I?", "What do you wear when it"
                 "gets cold?", "Guess the word: 'Sleeping ______ and the seven dwarves'?", "What's the opposite of "
                 "'tiny' and rhymes with defiant?", "Guess the word: 'I hopped out the shower and dried my self with "
                 "the _____'?", "Is the word 'gravity' spelt correctly?", "What language do they speak in France?",
                 "What language do they speak in America?",]
value = 0
answer_list = ["no", "yes", "yes", "no", "no", "no", "yes", "arrows", "ghost", "melbourne", "adelaide", "no", "yes",
               "house", "quiet", "money", "teacher","jumper", "beauty", "giant", "towel", "yes", "french", "english"]
fight_condition = True

while fight_condition is True:
    x = True
    level.Level.load_map(config.fight_scene_background)
    print("This enemy has challenged you to a fight!")
    # Display characters (both player and enemy)
    while x is True:
        print(question_list[value] + "\n")
        answer = input
        if answer.lower == answer_list[value]:
            # Run player attack
            print(""""Correct! You unleashed an attack upon your enemy!\n
                  Your enemy has been defeated""")
            X = False
        else:
            print("Incorrect! Your attack failed!!")
            # Run enemy attack
            player.Player.take_player_health(damage)
            value += 1
    fight_condition = False