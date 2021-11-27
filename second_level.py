from third_level import third_level_hinting, user_information, game_won, game_lost

latest_user_score = 0
latest_hint_number = 0


def second_level_hinting(random_number, hint_number, user_score, chance_number):
    global latest_user_score
    global latest_hint_number
    latest_hint_number = hint_number
    latest_user_score = user_score
    if random_number > 50:
        print(f"Hint {hint_number} : The number is greater than 50 . ")
        latest_hint_number += 1
        user_input_check(random_number, latest_hint_number, chance_number, user_score)
    else:
        print(f"Hint {hint_number} : The number is less than 50 . ")
        latest_hint_number += 1
        user_input_check(random_number, latest_hint_number, chance_number, user_score)


def user_input_check(random_number, hint_number, chance_number, user_score):
    user_input = int(input(f"Chance {chance_number}:"))
    chance_number += 1
    if user_input == random_number:
        game_won(user_score)
    else:
        print("You guessed wrong !!!")
        second_level_connect(random_number, hint_number, chance_number, user_score)


def second_level_connect(random_number, hint_number, chance_number, user_score):
    global latest_user_score
    latest_user_score -= 20
    print(f"Player_ID : {user_information['player_id']}" + " " * 5 + f"Score : {latest_user_score}")
    user_choice(random_number, hint_number, chance_number, user_score)


def user_choice(number, hint_number, chance_number, user_score):
    if not validity_check(chance_number):
        user_input = input("Do you want to try again or ask for next hint ? ( H for hint / C for chance )")
        if user_input.capitalize() == "H" and hint_number <= 3:
            third_level_hinting(number, hint_number, latest_user_score, chance_number)
        elif user_input.capitalize() == "C":
            user_input_check(number, hint_number, chance_number, user_score)
        elif user_input.capitalize() == "H" and hint_number > 3:
            print("You have taken all your hints . ")
            user_input_check(number, hint_number, chance_number, user_score)
    else:
        game_lost(number)


def validity_check(chance_number):
    if chance_number > 5:
        return True
    else:
        return False
