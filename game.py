from itertools import repeat
from random import choice
import os
from dotenv import load_dotenv

def determine_winner (player_name,computer_action):
    if u == computer_action:
        print(f"Both players selected {u}. It's a tie!")
    elif u == "rock": 
        if computer_action == "scissors" :
            print (f"Rock beats Scissors. {player_name} wins!")
        else:
            print (f"Paper beats Rock. {player_name} loses!")
    elif u == "paper": 
        if computer_action == "rock":
            print (f"Paper beats Rock! {player_name} wins!")
        else:
            print (f"Scissors beats Paper! {player_name} loses!") 
    elif u == "scissors": 
        if computer_action == "paper":
            print (f"Scissors beats Paper! {player_name} wins!")
        else:
            print (f"Rock beats Scissors! {player_name} loses!") 
    return 

if __name__ == "__main__":

    # WELCOME PLAYER 

    load_dotenv()
    player_name = os.getenv("PLAYER_NAME", default = "Player One")
    print("Welcome", player_name, "Let's Play Rock, paper, scissors!")

    # ASK FOR USER INPUT 
    u = input("Please choose one of: 'rock', 'paper', 'scissors':")
    print(player_name,"CHOSE:",u)

    # VALIDATIONS 
    u = u.lower()

    if u != 'rock' and u != 'paper' and u != 'scissors':
        print("Invalid choice: Please try again.")
        exit()
        
    # COMPUTER CHOICE 

    c = ['rock', 'paper', 'scissors']
    computer_action = choice(c)
    print("COMPUTER CHOSE:",computer_action)

    # DETERMINE THE WINNER 
    # DISPLAYING RESULTS

    determine_winner(u,computer_action)         

    # END GAME

    print(f"Thanks for playing {player_name}. Please play again!")
