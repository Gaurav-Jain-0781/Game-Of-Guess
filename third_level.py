latest_user_score = 0
user_information = {}


def user_info():
    name = input("Name :")
    age = input("Age  :")
    player_id = input("Player ID :")
    user_information["name"] = name.capitalize()
    user_information["age"] = age
    user_information["player_id"] = player_id


def user_number():
    number = int(input("For your third and last hind please give a number between 0 - 10 ? "))
    return number


def third_level_hinting(random_number, hint_number, user_score, chance_number):
    global latest_user_score
    latest_user_score = user_score
    number = random_number
    divisor = user_number()
    remainder = number % divisor
    print(f"Hint {hint_number} : The number subtracted {remainder} will be a multiple of {divisor} . ")
    user_input_check(random_number, hint_number, chance_number, user_score)


def user_input_check(random_number, hint_number, chance_number, user_score):
    user_input = int(input(f"Chance {chance_number}:"))
    chance_number += 1
    if user_input == random_number:
        game_won(user_score)
    else:
        print("You guessed wrong !!!")
        third_level_connect(random_number, hint_number, chance_number, user_score)


def third_level_connect(random_number, hint_number, chance_number, user_score):
    global latest_user_score
    latest_user_score -= 20
    print(f"player_ID : {user_information['player_id']}" + " "*5 + f"Score : {latest_user_score}")
    user_choice(random_number, hint_number, chance_number, user_score)


def user_choice(random_number, hint_number, chance_number, user_score):
    if not validity_check(chance_number):
        user_input = input("Do you want to try again or ask for next hint ? ( H for hint / C for chance )")
        if user_input.capitalize() == "C":
            user_input_check(random_number, hint_number, chance_number, user_score)
        elif user_input.capitalize() == "H":
            print("You have taken all your hints . ")
            user_input_check(random_number, hint_number, chance_number, user_score)
    else:
        game_lost(random_number)


def game_lost(random_number):
    print(f"player_ID : {user_information['player_id']}")
    print(f"Score : 0 ")
    print("You Lost !!!!!")
    print(f"The number was {random_number}")


def game_won(user_score):
    print(f"player_ID : {user_information['player_id']}")
    print(f"Score : {user_score}")
    print("Congratulations !!!!!")
    print("You guessed correctly .")
    print("\U0001F606" + "\U0001F606" + "\U0001F606")


def validity_check(chance_number):
    if chance_number > 5:
        return True
    else:
        return False
