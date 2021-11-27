from first_level import number_check, user_information, user_score, number
from third_level import user_info


def introduction():
    print("GAME OF GUESS")
    print("Hi there , Welcome to my ""GAME OF GUESS"" . ")
    print("Computer has chosen a number between 0 -100 . ")
    print("Before moving ahead I would like to take certain details regarding you . ")
    print("LET'S START !!!")
    user_info()
    print(f"Hi {user_information['player_id']} ")
    print("First let me you the rules of the game :\n"
          "1. Computer will decide a number by its own. \n"
          "2. You have to guess the number using various hints given from time to time .\n"
          "3. For each wrong guess your score will reduce by 20.\n"
          "4. Game will end at the right guess .\n"
          "5. All you have is 5 chances and 3 hints . \n "
          "LET'S BEGIN THE GAME \n ")
    print(f"Player_ID : {user_information['player_id']}" + " "*5 + f"Score : {user_score}")


introduction()
n = number_check(number)
print(n.check_prime())
print(n.non_prime_number())
