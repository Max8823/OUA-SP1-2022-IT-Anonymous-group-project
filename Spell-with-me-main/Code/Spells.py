import random
import operator
import math


class Spells:
    def _init_(self):
        self.answer = None
        question = None
        self.answers_list = [None]

    def make_question(self):
        return ''

    def check_Anwser(self, player_Answer):
        return True


# making a math spell
class math_spell(Spells):
    def __init__(self):

        self.make_question()

    def make_question(self):

        self.numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.functions = ["+", "-", "*", "/"]
        self.num1 = None
        self.operator_functions = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b,
        }
        self.answers_list = []
        self.num1 = random.randrange(1, len(self.numbers), 1)
        if self.num1 == 0:
            self.num1 += 1
        self.num2 = random.randrange(1, len(self.numbers), 1)
        if self.num2 > self.num1:
            while self.num2 > self.num1:
                self.num2 -= 1

        self.use_operator = self.functions[random.randrange(0, len(self.functions), 1)]

        self.answer = math.floor(self.operator_functions[self.use_operator](self.num1, self.num2))
        self.answers_list.append(self.answer)

        self.question = str(("what is " + str(self.num1) + " " + self.use_operator + " " + str(self.num2) + " ?"))

        while len(self.answers_list) < 4:

            num1 = random.randrange(1, len(self.numbers), 1)
            num2 = random.randrange(1, len(self.numbers), 1)

            if self.use_operator == '/' and (num1 or num2) == 0:
                num1 += 1
                num2 += 1

            a = math.floor(self.operator_functions[self.use_operator](num1, num2))

            if a == self.answer or a in self.answers_list:
                a = random.randrange(0, 20, 1)
            self.answers_list.append(a)

        random.shuffle(self.answers_list)
        return self.question, self.answers_list

    def check_Anwser(self, player_Answer):
        if self.answers_list[player_Answer] == self.answer:

            rep = True
        else:

            rep = False

        self.reset_question()
        return rep

    def reset_question(self):
        self.answer = None
        question = None
        self.answers_list = [None]


class spelling_spell(Spells):
    def make_question(self):

        spelling_questions_list = ["Is the word 'whistel' spelt correctly?", "Is the word 'knife' spelt correctly?",
                                   "Is the word 'wriggle' spelt correctly?", "Is the word 'rong' spelt correctly?",
                                   "Is the word 'gravity' spelt correctly?", "Is the word 'boosh' spelt correctly?",
                                   "Is the word 'triangle' spelt correctly?", "Does a 'which' cast spells?",
                                   "Does a " "'night' wear armour?",
                                   "Does 'their' describe something belonging to a person?",
                                   "Is the word 'knowledge' spelt correctly?", "Is 'where' a location word?"]

        spelling_answers_list = [0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1]
        self.answers_list = ["Yes", "No"]
        question_num = random.randrange(len(spelling_questions_list))
        question = spelling_questions_list[question_num]

        self.answer = spelling_answers_list[question_num]


        return question, self.answers_list

    def check_Anwser(self, player_Answer):

        if player_Answer == "yes":
            ans = 0
        else:
            ans = 1
        if ans == self.answer:

            rep = True
        else:
            rep = False

        self.reset_question()
        return rep

    def reset_question(self):
        self.answer = None
        question = None
        self.answers_list = [None]


class guess_spell(Spells):
    def make_question(self):
        questions_list = ["Guess the word: 'Sleeping ______ and the seven dwarves'?", "Guess the word: 'I hopped out "
                                                                                      "the shower and dried my self "
                                                                                      "with the _____'?",
                          "Guess the word: 'I hopped in the car and "
                          "_____ to the shop'", "Guess the word: 'It snows in the ______'?", "Guess the word: 'My dog "
                                                                                             "wears a ______ around it's neck'?",
                          "Guess the word: 'I hung my countries' ____ on the "
                          "pole'?", "Guess the word: 'Beauty and the _____'?", "Guess the word: 'A _______ is colorful,"
                                                                               " and comes out after it rains'?",
                          "Guess the word: 'I got my food out of the ______'?",
                          "Guess the word: 'Walking is too slow, instead I will ___'?", "What word do you live in and "
                                                                                        "rhymes with 'mouse'?", ]
        answer_list = ["Beauty", "Towel", "Drove", "Winter", "Collar", "Flag", "Beast", "Rainbow", "Fridge", "Run",
                       "House"]

        filler_list = ["Dog", "Angel", "Tree", "Rock", "Monkey", "Bathtub", "Window", "Sneezed", "Karate Kick", "Cat",
                       "Headphones", "Bottle", "Summer", "Jumper", "Kid", "Hammer", "Spring", "Carpark", "Ninja", "Sun",
                       "Bottle", "Shark", "Plant", "Phone", "Worn", "Walked", "Chopped", "Tissue", "Teddy Bear", "Gun",
                       "Road", "Truck", "Wax", "Sunglasses", "Swing", "Farted", "Cone", "Chicken", "Dance", "TV", "Hat",
                       "Ear", "Tail", "Slow", "Word", "List", "Maths", "Screen", "Roof", "Sky"]

        QA_num = random.randrange(len(questions_list))
        question = questions_list[QA_num]
        self.answer = answer_list[QA_num]
        self.answers_list = []
        self.answers_list.append(self.answer)

        while len(self.answers_list) < 4:
            a = filler_list[random.randrange(0, len(filler_list), 1)]
            if a in self.answers_list:
                a = filler_list[random.randrange(0, len(filler_list), 1)]
            self.answers_list.append(a)

        return question, self.answers_list

    def check_Anwser(self, player_Answer):
        if self.answers_list[player_Answer] == self.answer:


            rep = True
        else:

            rep = False

        self.reset_question()
        return rep

    def reset_question(self):
        self.answer = None
        question = None
        self.answers_list = [None]


class general_spell(Spells):

    def make_question(self):
        questions_list = ["What does an archer shoot out of his bow?", "What is white, scary, and says 'boo' at "
                                                                       "night?",
                          "What is the main city of Victoria?", "What is the main city of South "
                                                                "Australia?",
                          "What is the opposite of 'noisy' and rhymes with 'diet'?", "What do you use"
                                                                                     " to buy things with?",
                          "I help you to learn in class, what am I?", "What do you wear "
                                                                      "when it gets cold?",
                          "What's the opposite of 'tiny' and rhymes with defiant?",
                          "What language do they speak in France?", "What language do they speak in America?",
                          "What continent is Egypt in?"]

        answer_list = ["Arrows", "Ghost", "Melbourne", "Adelaide", "Quiet", "Money", "Teacher", "Jumper", "Giant",
                       "French", "English", "Africa"]

        filler_list = ["Road", "Truck", "Wax", "Sunglasses", "Swing", "Farted", "Cone", "Chicken", "Dance", "TV",
                       "Hat",
                       "Ear", "Tail", "Slow", "Word", "List", "Maths", "Screen", "Roof", "Sky", "Perth", "Sydney",
                       "Australia", "America", "Europe", "Russia", "Potato", "Onion", "Antartica", "Apple", "German",
                       "Japanese", "Mandarin", "Bus", "George", "Atlantis", "Knife", "Balloon", "London", "Euro",
                       "Music", "Croatia", "Jun-un", "Vladamir", "Cupboard", "Cloud", "Object", "Air",
                       "Business", "Trojan"]

        QA_num = random.randrange(0, len(questions_list), 1)
        question = questions_list[QA_num]
        self.answer = answer_list[QA_num]
        self.answers_list = []
        self.answers_list.append(self.answer)

        while len(self.answers_list) < 4:

            a = filler_list[random.randrange(0, len(filler_list), 1)]
            if a in self.answers_list:
                a = filler_list[random.randrange(0, len(filler_list), 1)]
            self.answers_list.append(a)

        return question, self.answers_list

    def check_Anwser(self, player_Answer):
        if self.answers_list[player_Answer] == self.answer:

            rep = True
        else:

            rep = False

        self.reset_question()
        return rep

    def reset_question(self):
        self.answer = None
        question = None
        self.answers_list = [None]
