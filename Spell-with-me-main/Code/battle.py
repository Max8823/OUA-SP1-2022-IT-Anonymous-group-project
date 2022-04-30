import pygame
from player import *
from Inventory import Inventory
from enemy_class import *
import Item
import level
import config

battle_status = False
player = object
enemy = object

class battle:
    def __init__(self):

        self.player = object
        self.enemy = object
        self.loot = None
        self.turn = 'player'
        self.result = False
        self.map0_background = pygame.image.load('../graphics/maps/0/Forest_Fight.png').convert_alpha()


        self.screen = pygame.display.get_surface()

    def set_battle(self, player1, enemy1):
        global player, enemy

        player = player1
        enemy = enemy1

    def set_battle_status(self, status):
        global battle_status
        battle_status = status

    def get_battle_status(self):
        global battle_status
        return battle_status


    def end_battle(self):
        global battle_status
        battle_status = False

        self.set_battle_loot(enemy.get_loot())
        pygame.sprite.Sprite.kill(enemy)

        self.set_result(True)

        #will shove enemy to 0:0
        enemy.set_enemy_pos()

    def set_battle_loot(self, loot):
        loot_list = list(loot)
        player_known = player.get_player_learned_spells()
        while loot_list[0] in player_known:

            loot_list[0] = random.randrange(0, 9, 1)

        self.loot = loot_list



    def get_battle_loot(self):
        return self.loot

    def get_result(self):
        return self.result

    def set_result(self, result):
        self.result = result

    def draw_battle(self):
        #chaneg to background image / could be random 1 of 3? or 1 per map?


            self.screen.blit(self.map0_background, (0,0))

            self.screen.blit(player.get_player_image(), (450, 550))
            self.screen.blit(enemy.get_enemy_image(), (500, 500))

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
                     "Australia?", "Is the word 'knowlege' spelt correctly?", "Is 'where' a location word?", "What word"
                     " do you live in and rhymes with 'mouse'?", "What is the opposite of 'noisy' and rhymes with "
                     "'diet'?", "What do you use to buy things with?", "I help you to learn in class, what am I?",
                     "What do you wear when it gets cold?", "Guess the word: 'Sleeping ______ and the seven dwarves'?",
                     "What's the opposite of 'tiny' and rhymes with defiant?", "Guess the word: 'I hopped out the "
                     "shower and dried my self with a _____'?", "Is the word 'gravity' spelt correctly?", "What "
                     "language do they speak in France?", "What language do they speak in America?" ]
    value = 0
    answer_list = ["no", "yes", "yes", "no", "no", "no", "yes", "arrows", "ghost", "melbourne", "adelaide", "no", "yes",
                   "house", "quiet", "money", "teacher", "jumper", "beauty", "giant", "towel", "yes", "french", "english"]
    fight_condition = True

    while fight_condition is True:
        x = True
        draw_arena()
        print("This enemy has challenged you to a fight!")
        get_battle_players()
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
