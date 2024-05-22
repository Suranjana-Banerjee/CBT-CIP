import random
user_choice= int(input('Enter your choice (0 for Rock, 1 for Paper, 2 for Scissor)::'))
if user_choice > 2 or user_choice < 0:
    print("Invalid Choice, Try Again!")
else:
    computer_choice= random.randint(0,2)
    print('Computer Chose::', computer_choice)
    if user_choice == computer_choice:
        print("It's a draw.")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose.")
    elif computer_choice == 2 and user_choice == 0:
        print("You Win.")
    elif computer_choice > user_choice:
        print("You lose.")
    elif computer_choice < user_choice:
        print("You Win.")
