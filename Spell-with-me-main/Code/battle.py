import pygame
from player import *
from enemy_class import *
import Spells
from Item import Item
from Inventory import Inventory
import user_interactions

font = pygame.freetype.Font(pygame.font.match_font("calibiri"), 26)

battle_status = False
player = object
enemy = object
map_code = int
answer_pos = []
active_spell = None
sucessful_cast = None
answer = None
current_spell = None
battle_result = None

spell_pos = []
spells = []
answer_list = []
turn = 'player'


class battle:
	def __init__(self):

		self.player = object
		self.enemy = object
		self.loot = None
		self.turn = 'player'
		self.result = None
		self.keys = pygame.key.get_pressed()

		self.Math_spell = Spells.math_spell()
		self.Spelling_spell = Spells.spelling_spell()
		self.guess_spell = Spells.guess_spell()
		self.gen_spell = Spells.general_spell()

		self.screen = pygame.display.get_surface()
		self.load_img()
		self.question_details = None
		self.question = None
		self.answer_list = [None]
		self.player_answer = None

		self.spells = []

		self.inventory = Inventory()
		self.item = Item


		self.screen = pygame.display.get_surface()

	def set_battle(self, player1, enemy1, map_num):
		global player, enemy, map_code, turn, battle_result

		player = player1
		turn = 'player'
		enemy = enemy1
		map_code = map_num
		enemy.set_battle(True)
		enemy.draw_enemy_health()
		player.set_battle(True)
		battle_result = None
		pygame.display.update()

	def set_battle_status(self, status):
		global battle_status

		battle_status = status

	def get_battle_status(self):
		global battle_status

		return battle_status

	def set_turn(self):
		global turn
		turn = None

	def end_battle(self, passed_result):
		global active_spell, sucessful_cast, answer, answer_list, spell_pos, spells, current_spell, turn
		global battle_status

		self.question_details = None
		self.question = None
		self.answer_list = [None]
		self.player_answer = None
		active_spell = None
		sucessful_cast = None
		answer = None
		current_spell = None
		spell_pos = []
		spells = []
		answer_list = []
		turn = None

		self.set_battle_loot(enemy.get_loot())
		pygame.sprite.Sprite.kill(enemy)

		enemy.set_battle(False)
		player.set_battle(False)
		battle_status = False

		self.set_result(passed_result)


		# will shove enemy to 0:0
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
		global battle_result

		return battle_result

	def set_result(self, passed_result):
		global battle_result
		battle_result = passed_result

	def reset_question(self):
		global active_spell, sucessful_cast, answer, answer_list, spell_pos, spells, current_spell, battle_result
		self.question_details = None
		self.question = None
		self.answer_list = [None]
		self.player_answer = None
		battle_result = None
		active_spell = None
		sucessful_cast = None
		answer = None
		current_spell = None
		spell_pos = []
		spells = []
		answer_list = []


	def draw_battle(self):
		global answer_pos, answer, spell_pos, current_spell, turn, inven_open, battle_status
		if battle_status:
			self.x = 400
			self.y = 580
			self.spell_x = 400
			self.spell_y = 580
			self.screen.blit(pygame.image.load('../graphics/maps/' + str(map_code) + '/battle_scene.png').convert_alpha(),
			                 (0, 0))
			self.screen.blit(player.get_player_image(), (450, 550))
			self.screen.blit(enemy.get_enemy_image(), (500, 500))

			self.screen.blit(self.battle_ui, (0, 240))
			self.screen.blit(self.exit_button, (20, 500))
			self.screen.blit(self.pot_button, (30, 375))
			i = 0

			potions = self.inventory.get_items_list()
			for item in potions:

				if potions[i].get_item_code() == 0:
					count = potions[i].get_item_count()
					if count is None:
						count = 0
					text_surface, rect = font.render(str(count), (255, 0, 0))
					self.screen.blit(text_surface, (30, 380))
				i += 1

			self.screen.blit(self.battle_ui_buttom, (300, 480))

			if turn == 'player':
				text_surface, rect = font.render(str("Player Turn"), (0, 0, 0))
				self.screen.blit(text_surface, (640, 100))

				if not current_spell:
					self.spells = player.get_player_spells()
					i = 0
					for spell in self.spells:
						if self.spells[spell]["learnt"]:
							self.screen.blit(self.spell_slot, (self.spell_x, self.spell_y))
							self.screen.blit(self.spells[spell]["img"], (self.spell_x + 20, self.spell_y + 15))
							if len(spell_pos) < len(self.spells):
								spell_pos.append((self.spell_x, self.spell_y))
							self.spell_x += 108

				else:
					text_surface, rect = font.render(str("Casting " + str(current_spell)), (0, 0, 0))
					self.screen.blit(text_surface, (640, 150))
					if self.question_details is None:
						self.question_details = self.get_question()
						self.question = self.question_details[0]
						self.answer_list = self.question_details[1]
					i = 0
					for answer in self.answer_list:

						text_surface, rect = font.render(str(self.question), (0, 0, 0))
						self.screen.blit(text_surface, (400, 500))

						self.screen.blit(self.answer_button, (self.x, self.y))

						text_surface, rect = font.render(str(answer), (0, 0, 0))
						self.screen.blit(text_surface, (self.x + 5, self.y + 5))

						if len(answer_pos) <= len(self.answer_list):
							answer_rect = self.answer_button.get_rect()
							answer_pos.append((self.x, self.y))
							i += 1
						self.x += 150
				self.player_turn()

			elif turn == 'enemy':
				text_surface, rect = font.render(str("Enemy Turn"), (0, 0, 0))
				self.screen.blit(text_surface, (640, 100))
				self.enemy_turn()

			else:
				pygame.display.update()
				self.check_status()


	def check_status(self):
		global turn
		if player.get_current_health() <= 0:
			self.end_battle(False)
			self.update()
			self.screen.fill('black')
			self.screen.blit(self.lose_msg, (440, 100))
			self.update()
			self.wait()


		elif enemy.get_enemy_health() <=0 :
			self.end_battle(True)
			self.update()
			self.screen.fill('black')
			self.screen.blit(self.win_msg, (440,100))
			self.update()

			self.inventory.add_item(self.get_battle_loot()[0], self.get_battle_loot()[1])
			self.inventory.add_item(0, 2)
			self.wait()

	def player_turn(self):
		global sucessful_cast, answer, current_spell, turn, battle_result
		battle_result = None

		if pygame.mouse.get_pressed()[0]:
			mouse_pos = pygame.mouse.get_pos()
			if mouse_pos[0] > 400:
				if current_spell is None:
					user_choice = self.get_user_selection(mouse_pos, 1)

				elif current_spell is not None:
					self.user_choice = self.get_user_selection(mouse_pos, 0)
					if self.user_choice is not None:
						result = self.check_answer(self.user_choice)
						if result:
							sucessful_cast = True
							self.spell_result()
							self.attack()
							self.reset_question()
							self.wait()
							self.check_status()
							turn = 'enemy'

						else:
							sucessful_cast = False
							self.spell_result()
							self.reset_question()
							self.wait()
							self.check_status()
							turn = 'enemy'

			else:
				self.user_choice = self.get_user_selection(mouse_pos, 2)

	def get_user_selection(self, mouse_pos, type):
		global current_spell
		self.match = None

		if type == 0:
			answers_pos = self.get_answer_pos()
			dist = 30
			i = 0
			for answer in answers_pos:

				item_pos_x = answers_pos[i][0]
				item_pos_y = answers_pos[i][1]

				if abs((((((item_pos_x + 126) - item_pos_x) / 2) + item_pos_x) - mouse_pos[0])) <= 63 and abs(
						(((((item_pos_y + 79) - item_pos_y) / 2) + item_pos_y) - mouse_pos[1])) <= 40:
					self.match = i
				else:
					i += 1

		else:
			answers_pos = self.get_spell_pos()

			i = 0
			match = None
			for answer in answers_pos:

				item_pos_x = answers_pos[i][0]
				item_pos_y = answers_pos[i][1]

				if abs((((((item_pos_x + 55) - item_pos_x) / 2) + item_pos_x) - mouse_pos[0])) <= 32 and abs(
						(((((item_pos_y + 55) - item_pos_y) / 2) + item_pos_y) - mouse_pos[1])) <= 32:
					self.match = i
					spells_tmp = player.get_player_spells()
					for spell in spells_tmp:
						if spells_tmp[spell]["learnt"]:
							spells.append(spell)
					current_spell = spells[self.match]

				else:
					i += 1

		return self.match

	def get_answer_pos(self):
		global answer_pos

		return answer_pos

	def get_spell_pos(self):
		global spell_pos

		return spell_pos

	def attack(self):
		global current_spell

		spells_tmp = player.get_player_spells()

		if current_spell in spells_tmp:
			damage = int(spells_tmp[current_spell]["damage"])
			enemy.set_enemy_health(damage)
			self.update()

	def spell_result(self):
		global current_spell
		if sucessful_cast:
			text_surface, rect = font.render(str("sucessfully cast " + str(current_spell)), (0, 0, 0))
			self.screen.blit(text_surface, (640, 200))
			self.screen.blit(self.spells[current_spell]["img"], (640, 250))

		if not sucessful_cast:
			if sucessful_cast is None:
				""
			else:
				text_surface, rect = font.render(str("Failed to cast " + str(current_spell)), (0, 0, 0))
				self.screen.blit(text_surface, (640, 200))
				self.screen.blit(self.spells[current_spell]["img"], (640, 250))

		self.update()

	def update(self):
		pygame.display.flip()
		pygame.display.update()

	def get_question(self):
		global active_spell
		selection = random.randrange(0, 4, 1)

		if selection == 0:
			active_spell = 'math'

			question = self.Math_spell.make_question()

		elif selection == 1:
			active_spell = 'Spelling'

			question = self.Spelling_spell.make_question()
		elif selection == 2:
			active_spell = 'guess'

			question = self.guess_spell.make_question()
		else:
			active_spell = 'general'

			question = self.gen_spell.make_question()

		return question

	def enemy_turn(self):
		global turn

		enemy_spells_tmp = enemy.get_enemy_spells()
		spell_no = None
		spell_name = None

		spell_no = random.randrange(0, len(enemy_spells_tmp), 1)
		enemy_spells = []
		for enemy_spell in enemy_spells_tmp:
			enemy_spells.append(enemy_spell)
		i = 0
		for enemy_spell in enemy_spells_tmp:
			if spell_no == enemy_spells_tmp[enemy_spell]["spell_id"]:
				spell_name = enemy_spells[i]
			else:
				i += 1

		dmg = random.randrange(0, enemy_spells_tmp[spell_name]["damage"], 1)
		player.set_player_health(dmg)

		text_surface, rect = font.render(
			str(enemy.get_enemy_name() + " used " + spell_name + " and did " + str(dmg) + " damage"), (0, 0, 0))
		self.screen.blit(text_surface, (640, 200))
		self.update()
		self.wait()
		self.check_status()
		turn = 'player'

	def check_answer(self, user_answer):
		global active_spell

		if active_spell == 'math':

			response = self.Math_spell.check_Anwser(user_answer)

		elif active_spell == 'Spelling':

			response = self.Spelling_spell.check_Anwser(user_answer)

		elif active_spell == 'guess':

			response = self.guess_spell.check_Anwser(user_answer)
		else:
			active_spell = 'general'

			response = self.gen_spell.check_Anwser(user_answer)

		return response

	def get_current_spell(self):
		global current_spell

		return current_spell

	def wait(self):
		self.update()
		pygame.time.wait(3000)

	def load_img(self):

		self.answer_button = pygame.image.load('../graphics/battle/question_slot.png').convert_alpha()
		self.exit_button = pygame.image.load('../graphics/battle/exit_button.png').convert_alpha()
		self.pot_button = pygame.image.load('../graphics/items/small/hp_potion.png').convert_alpha()
		self.battle_ui = pygame.image.load('../graphics/battle/battle_ui.png').convert_alpha()
		self.battle_ui_buttom = pygame.image.load('../graphics/battle/battle_ui_bottom.png').convert_alpha()
		self.spell_slot = pygame.image.load('../graphics/inventory/Spell_box.png').convert_alpha()
		self.continue_button = pygame.image.load('../graphics/battle/continue.png').convert_alpha()
		self.win_msg = pygame.image.load('../graphics/battle/win_msg.png').convert_alpha()
		self.lose_msg = pygame.image.load('../graphics/battle/lose_msg.png').convert_alpha()
