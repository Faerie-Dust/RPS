# Authors: Ali Rizvi and Vanessa Trinh
# Purpose: A simple Rock Paper Scissors game written for the Global Hackathon Week challenges
# Date: 05/01/2023

import random

RPS_MOVES = [
    "rock",
    "paper",
    "scissors"
]

MOVE_WINNERS = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

def randomMove():
    computerMove = random.choice(RPS_MOVES)
    return computerMove
    

if __name__ == "__main__":
    print("Select either rock, paper, or scissor.", "The computer will do its best to try and beat your score!", "", sep="\n")

    score = 0
    highscore = 0
    
    while True:
        print("1) Rock", "2) Paper", "3) Scissors", "*) Exit", "", sep="\n")
        
        userMove = ""
        computerMove = randomMove()
        opt = input("Enter your choice: ")
        
        if opt.isdigit() and 3 >= (num := int(opt)) >= 1:
            userMove = RPS_MOVES[num - 1]
            if userMove == computerMove:
                print(f"Both picked {userMove}. You tied!")
            elif MOVE_WINNERS[userMove] == computerMove:
                print(f"{userMove.capitalize()} beats {computerMove}. You beat the computer! :>")
                print(f"Your score is now {score :+= 1}")
            else:
                print(f"{computerMove.capitalize()} beats {userMove}. You lost. :c")
            
            if (choice := input("Would you like to play again [y/N]? ")).lower() == "y":
                pass
            else:
                break
        else:
            break
    
    print("Exiting, have a good day!")