from itertools import repeat
from random import choice
import os

# WELCOME PLAYER 

player_name = os.getenv("PLAYER_NAME", default = "Player One")
print("Welcome"); player_name; print("Let's Play Rock, paper, scissors!")

# ASK FOR USER INPUT 
u = input("Please choose one of: 'rock', 'paper', 'scissors':")
print("USER CHOSE:",u)

# VALIDATIONS 
u = u.lower()

if u != 'rock' and u != 'paper' and u != 'scissors':
    print("Invalid choice: Please select again.")
    exit()
    
# COMPUTER CHOICE 

c = ['rock', 'paper', 'scissors']
computer_action = choice(c)
print("THE COMPUTER CHOSE:",computer_action)

# DETERMINE THE WINNER 
# DISPLAYING RESULTS

def determine_winner(u, computer_action):
    """
    Determines the winning choice between two valid choices from selectable options: "rock", "paper", or "scissors".

    Returns the winning choice (e.g. "paper"), or None if there is a tie.

    Example: determine_winner("rock", "paper")
    """
    # todo: write some Python here to determine the winner
    return "TODO"


if __name__ == "__main__":

    print("WELCOME TO MY ROCK PAPER SCISSORS GAME!")

    # ...     

from game import determine_winner

def test_determination_of_the_winner():
    assert determine_winner("rock", "rock") == None # represents a tie
    assert determine_winner("rock", "paper") == "paper"
    assert determine_winner("rock", "scissors") == "rock"

    assert determine_winner("paper", "rock") == "paper"
    assert determine_winner("paper", "paper") == None # represents a tie
    assert determine_winner("paper", "scissors") == "scissors"

    assert determine_winner("scissors", "rock") == "rock"
    assert determine_winner("scissors", "paper") == "scissors"
    assert determine_winner("scissors", "scissors") == None # represents a tie

# END GAME

print("Thanks for playing. Please play again!")