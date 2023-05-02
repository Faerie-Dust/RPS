import os
import curses
import random
import pathlib

CPU_SCORE = 0
USER_SCORE = 0

HIGHSCORE = 0

HIGHSCORE_FILE = pathlib.Path(pathlib.Path(__file__).parent, "highscore.dat")

MOVES = [
    "rock",
    "paper",
    "scissors"
]

WINNING_MATCHUPS = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

def show_scores(stdscr: 'curses._CursesWindow'):
    score_text = f"Your score: {USER_SCORE} | CPU score: {CPU_SCORE}"
    highscore_text = f"High Score: {HIGHSCORE}"

    stdscr.addstr(0, curses.COLS - len(score_text), score_text)
    stdscr.addstr(1, curses.COLS - len(highscore_text), highscore_text)

def main_screen(stdscr: 'curses._CursesWindow'):

    stdscr.clear()

    stdscr.addstr(0, 0, "To get started, select one of the options below")
    stdscr.addstr(1, 0, "After choosing you will compete with the computer's result")
    stdscr.addstr(3, 0, "1) Rock")
    stdscr.addstr(4, 0, "2) Paper")
    stdscr.addstr(5, 0, "3) Scissors")
    stdscr.addstr(6, 0, "q) Exit")
    stdscr.addstr(8, 0, "Enter your choice: ")

    show_scores(stdscr)

    stdscr.refresh()

def main(stdscr: 'curses._CursesWindow'):
    global CPU_SCORE, USER_SCORE, HIGHSCORE

    cpuMove         = ""
    userMove        = ""
    numberChoice    = 0
    playAgainChoice = "y"

    if os.path.exists(HIGHSCORE_FILE):
        with open(HIGHSCORE_FILE, "r") as f:
            HIGHSCORE = int(f.readline())

    while playAgainChoice == "y":
        main_screen(stdscr)

        while True:
            choice = stdscr.getch()
            numberChoice = choice - ord('0')

            if 3 >= numberChoice >= 1:
                cpuMove  = random.choice(MOVES)
                userMove = MOVES[numberChoice - 1]

                break
            elif choice == ord('q'):
                stdscr.clear()
                stdscr.addstr(0, 0, "Exiting, have a nice day!")
                stdscr.refresh()

                break

        if choice != ord("q"):
            stdscr.clear()

            if userMove == cpuMove:
                stdscr.addstr(0, 0, f"Both picked {userMove}. You tied!")
            elif WINNING_MATCHUPS[userMove] == cpuMove:
                USER_SCORE += 1
                stdscr.addstr(0, 0, f"{userMove.capitalize()} beats {cpuMove}. You beat the computer! :>")
            else:
                CPU_SCORE += 1
                stdscr.addstr(0, 0, f"{userMove.capitalize()} loses to {cpuMove}. You lost. :c")

            show_scores(stdscr)
            stdscr.addstr(1, 0, "Would you like to play again [y/N]? ")

            playAgainChoice = chr(stdscr.getch())

            stdscr.refresh()
        else:
            break

    stdscr.clear()
    show_scores(stdscr)


    HIGHSCORE = max(HIGHSCORE, USER_SCORE) # replaces highscore with the higher value
    with open(HIGHSCORE_FILE, "w") as f:
        f.writelines(str(HIGHSCORE))

    if HIGHSCORE <= USER_SCORE:
        stdscr.addstr(0, 0, f"Congrats! Your new high score is {HIGHSCORE}!")
    else:
        stdscr.addstr(0, 0, f"You didn't beat your high score of {HIGHSCORE}, better luck next time!")
    stdscr.addstr(1, 0, "Exiting, have a nice day!")
    stdscr.refresh()
    curses.napms(2000)

if __name__ == "__main__":
    curses.wrapper(main)