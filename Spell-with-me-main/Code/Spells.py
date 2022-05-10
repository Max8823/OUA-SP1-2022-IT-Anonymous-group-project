import pygame
import random


class spells:
    def _init_(self):
        self.answer
        self.questions = []

    def create_question(self):
        return ""


    def check_answer(self, player_answer):
        return True

class math_spell(spells):

    def make_question(self):
        self.numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.operators = ["+", "-", "/", "*"]
        num1 = random.randrange(0,len(self.numbers),1)
        num2 = random.randrange(0, len(self.numbers), 1)
        use_operator = random.randrange(0, len(self.operators), 1)
        math_question = "What is ", num1, use_operator, num2, "?"
        answer = num1, use_operator, num2
        answer_list = []
        answer_list.append(answer)
        while len(answer_list) < 3:
            a = random.randrange(0, len(self.numbers), 1), use_operator, (0, len(self.numbers), 1)
            answer_list.append(a)
            a = 0
        return math_question, answer_list


    def guess_question(self):
        # 11 Questions and answers
        questions_list = ["Guess the word: 'Sleeping ______ and the seven dwarves'?", "Guess the word: 'I hopped out "
                          "the shower and dried my self with the _____'?", "Guess the word: 'I hopped in the car and "
                          "_____ to the shop'", "Guess the word: 'It snows in the ______'?", "Guess the word: 'My dog "
                          "wears a ______ around it's neck'?", "Guess the word: 'I hung my countries' ____ on the "
                          "pole'?", "Guess the word: 'Beauty and the _____'?", "Guess the word: 'A _______ is colorful,"
                          " and comes out after it rains'?", "Guess the word: 'I got my food out of the ______'?",
                          "Guess the word: 'Walking is too slow, instead I will ___'?", "What word do you live in and "
                          "rhymes with 'mouse'?",]
        answers_list = ["Beauty", "Towel", "Drove", "Winter", "Collar", "Flag", "Beast", "Rainbow", "Fridge", "Run",
                        "House"]
        filler_list = ["Dog", "Angel", "Tree", "Rock", "Monkey", "Bathtub", "Window", "Sneezed", "Karate Kick", "Cat",
                       "Headphones", "Bottle", "Summer", "Jumper", "Kid", "Hammer", "Spring", "Carpark", "Ninja", "Sun",
                       "Bottle", "Shark","Plant", "Phone", "Worn", "Walked", "Chopped", "Tissue", "Teddy Bear", "Gun",
                       "Road", "Truck", "Wax", "Sunglasses", "Swing", "Farted", "Cone", "Chicken", "Dance", "TV", "Hat",
                       "Ear", "Tail", "Slow", "Word", "List", "Maths", "Screen", "Roof", "Sky"]
        multiple_answers_list = [answers_list(), random.randrange(len(filler_list)), random.randrange(len(filler_list)),
                                 random.randrange(len(filler_list))]
        question = random.randrange(len(questions_list))
        answer_number = questions_list(question)
        answer = answers_list(answer_number)
        return question, multiple_answers_list

    def spelling_and_grammar_questions(self):
        # 12 questions and answers
        spelling_questions_list = ["Is the word 'whistel' spelt correctly?", "Is the word 'knife' spelt correctly?",
                                   "Is the word 'wriggle' spelt correctly?", "Is the word 'rong' spelt correctly?",
                                   "Is the word 'gravity' spelt correctly?", "Is the word 'boosh' spelt correctly?",
                                   "Is the word 'triangle' spelt correctly?", "Does a 'which' cast spells?", "Does a "
                                   "'night' wear armour?", "Does 'their' describe something belonging to a person?",
                                   "Is the word 'knowlege' spelt correctly?", "Is 'where' a location word?"]
        spelling_answers_list = [1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1]
        filler_list2 = ["Yes", "No"]
        question = random.randrange(len(spelling_questions_list))
        answer_num = spelling_questions_list(question)
        answer_num2 = spelling_answers_list(answer_num)
        answer = filler_list2(answer_num2)
        return question, filler_list2, answer

    def general_questions(self):
        # 10 questions and answers
        gen_questions_list = ["What does an archer shoot out of his bow?", "What is white, scary, and says 'boo' at "
                              "night?", "What is the main city of Victoria?", "What is the main city of South "
                              "Australia?", "What is the opposite of 'noisy' and rhymes with 'diet'?", "What do you use"
                              " to buy things with?", "I help you to learn in class, what am I?", "What do you wear "
                              "when it gets cold?", "What's the opposite of 'tiny' and rhymes with defiant?",
                              "What language do they speak in France?", "What language do they speak in America?",
                              "What continent is Egypt in?"]
        gen_answers_list = ["Arrows", "Ghost", "Melbourne", "Adelaide", "Quiet", "Money", "Teacher", "Jumper", "Giant",
                            "French", "English", "Africa"]
        filler_list3 = ["Road", "Truck", "Wax", "Sunglasses", "Swing", "Farted", "Cone", "Chicken", "Dance", "TV", "Hat",
                        "Ear", "Tail", "Slow", "Word", "List", "Maths", "Screen", "Roof", "Sky", "Perth", "Sydney",
                        "Australia", "America", "Europe", "Russia", "Potato", "Onion", "Antartica", "Apple", "German",
                        "Japanese", "Mandarin", "Bus", "George", "Atlantis", "Knife", "Balloon", "London", "Euro",
                        "Music", "Croatia", "Kim Jun-un", "Vladamir Putin", "Cupboard", "Cloud", "Object", "Air",
                        "Business", "Trojan Horse"]
        multiple_answers_list = [answers_list(), random.randrange(len(filler_list)), random.randrange(len(filler_list)),
                                 random.randrange(len(filler_list))]
        question = random.randrange(len(questions_list))
        answer_number = gen_questions_list(question)
        answer = gen_answers_list(answer_number)
        return question, multiple_answers_list




