from random import randint
from second_level import second_level_hinting, user_information
from third_level import game_won, game_lost

hint_number = 1
chance_number = 1

divisible_by = []

user_score = 100
number = randint(0, 100)


class number_check:
    def __init__(self, number):
        self.number = number

    def check_prime(self):
        global hint_number
        if self.number > 1:
            for i in range(2, self.number):
                if self.number % i == 0:
                    break
            else:
                print(f"Hint {hint_number} : The number is a prime number .")
                hint_number += 1
                return user_input_check(self.number)

    def non_prime_number(self):
        if self.number > 1:
            for i in range(2, self.number+1):
                if self.number % i == 0:
                    divisible_by.append(i)
        return first_level_hint(divisible_by, self.number)


def first_level_hint(numbers_list, answer):
    global hint_number
    if len(numbers_list) >= 4:
        print(f"Hint {hint_number} : The number has {numbers_list[0]}, {numbers_list[1]}, {numbers_list[2]} "
              f"as its lowest common factors .")
        hint_number += 1
        user_input_check(answer)
    elif len(numbers_list) == 3:
        print(f"Hint {hint_number} : The number is divisible by {numbers_list[0]}, {numbers_list[1]} . ")
        hint_number += 1
        user_input_check(answer)
    elif len(numbers_list) == 2:
        print(f"Hint {hint_number} : The number has only two common factors except 1 . ")
        hint_number += 1
        user_input_check(answer)


def user_input_check(actual_number):
    global chance_number
    user_input = int(input(f"Chance {chance_number} :"))
    chance_number += 1
    if user_input == actual_number:
        game_won(user_score)
    else:
        print("You guessed wrong !!!")
        first_level_connect()


def first_level_connect():
    global user_score
    user_score -= 20
    print(f"Player_ID : {user_information['player_id']}" + " "*5 + f"Score : {user_score}")
    user_choice()


def user_choice():
    if not validity_check():
        user_input = input("Do you want to try again or ask for next hint ? ( H for hint / C for chance )")
        if user_input.capitalize() == "H" and hint_number <= 3:
            second_level_hinting(number, hint_number, user_score, chance_number)
        elif user_input.capitalize() == "C":
            user_input_check(number)
        elif user_input.capitalize() == "H" and hint_number > 3:
            print("You have taken all your hints . ")
            user_input_check(number)
    else:
        game_lost(number)


def validity_check():
    if chance_number > 5:
        return True
    else:
        return False
