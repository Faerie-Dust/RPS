import curses
import random

CPU_SCORE  = 0
USER_SCORE = 0

HIGHSCORE  = 0

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

def main_screen(stdscr: 'curses._CursesWindow'):
    score_text = f"Your score: {USER_SCORE} | CPU score: {CPU_SCORE}"

    stdscr.clear()

    stdscr.addstr(0, 0, "To get started, select one of the options below")
    stdscr.addstr(0, curses.COLS - len(score_text), score_text)
    stdscr.addstr(1, 0, "After choosing you will compete with the computer's result")
    stdscr.addstr(3, 0, "1) Rock")
    stdscr.addstr(4, 0, "2) Paper")
    stdscr.addstr(5, 0, "3) Scissors")
    stdscr.addstr(6, 0, "q) Exit")
    stdscr.addstr(8, 0, "Enter your choice: ")

    stdscr.refresh()

def choice_loop(stdscr: 'curses._CursesWindow'):
    while True:
        choice = stdscr.getch() - ord('1')

        y, x = stdscr.getyx()
        if 3 >= choice >= 1:
            stdscr.addch(y, x, str(choice))
            #return MOVES[choice]


def main(stdscr: 'curses._CursesWindow'):
    cpuMove  = random.choice(MOVES)
    userMove = None

    main_screen(stdscr)

    while True:
        choice = stdscr.getch()

        if 3 >= (num := int(choice)) >= 1:
            userMove = MOVES[num - 1]
            if userMove == cpuMove:
                print(f"Tied!")
            elif WINNING_MATCHUPS[userMove] == cpuMove:
                print("u beat cpu!")
            else:
                print("cpu beat u!")

        elif choice == ord('q'):
            stdscr.clear()
            stdscr.addstr(0, 0, "Exiting, have a nice day!")
            stdscr.refresh()

            break

    curses.napms(2000)

if __name__ == "__main__":
    curses.wrapper(main)
