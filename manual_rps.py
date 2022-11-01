'''
This file is used to play Rock Paper Scissors without a camera.

Two functions: get_computer_choice and get_user_choice. 
get_computer_choice will randomly pick an option between "Rock", "Paper", and "Scissors" and return the choice. 
get_user_choice will ask the user for an input and return it.

Both functions uses the ranom module to pick a random choice between rock, paper, and scissors.

'''

import random

def get_computer_choice():
    choice = ["rock", "paper", "scissors"]
    computer_choice =  random.choice(choice)
    # print(f"Computer chooses: {computer_choice}.") # For testing only
    return computer_choice

def get_user_choice():
    try:
        while True:
            choice = ["rock", "paper", "scissors"]
            user_choice = input('Please enter one of the following: "Rock", "Paper", "Scissors"').lower()
            if user_choice in choice:
                break
            else:
                print('Not a valid entry!')
        return user_choice
    except:
        print("error")

# Task 2 Figuring out who won. Using if-elif-else statement

def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        result = "Draw"
    # Combinations for user to win
    elif (computer_choice == "rock" and user_choice == "paper") or (computer_choice == "paper" and user_choice == "scissors"):
        result = "User Wins!"
    # All other Combinations means Computer wins
    else:
        result = "Computer Wins!"
    print(result)
    return result


# Now wraping it all up in one function, play().
def play():
    '''
    Wrapping up all the functions created into one function that runs the game
    '''
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    print(f"for testing only - computer: {computer_choice} - user: {user_choice}")
    get_winner(computer_choice, user_choice)



def main():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    winner = get_winner(computer_choice, user_choice)

if __name__ == "__main__":
    main()#Executed when invoked directly
# %%



