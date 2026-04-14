# import necessary modules
import random 
import os 
import time

# variables that defines the rules of the game
ROWS = 6
COLS = 6
NUM_PLAYERS = 2
CHECKERS = ["X", "O"]

# 6x6 board
board = []
for r in range(ROWS):
    board.append([" "] * COLS)

# randomly choosing the first player
current_player = random.randint(0, NUM_PLAYERS - 1)

# variables that keeps track of the game's progress
game_over = False

# keep asking for coordinates until no empty spaces are left
while not game_over:
    os.system("clear")

# print the column letters
    print("   ", end="")
    for c in range(COLS):
        print(chr(65 + c), end='   ')
    print("\n  +" + "---+" * COLS)

# prints the row numbers and the cells of the board
    for r in range(ROWS):
        print(str(r) + " |", end="")
        for c in range(COLS):
            print(" " + board[r][c] + " |", end="")
        print("\n  +" + "---+" * COLS)

    checker = CHECKERS[current_player]

# user input
    guess = input("Player " + str(current_player + 1) + " (" + checker + "), enter coordinates (e.g. A0): ")

# checks if the input is too short   
    if len(guess) < 2:
        print("Invalid! Format must be a letter then a number.")
        time.sleep(1)
        continue

# split the input into the letter part and the number part
    column_letter = guess[0] 
    row_number = guess[1:]

# makes sure the row is a number and the column is a letter
    if not row_number.isdigit() or not column_letter.isalpha():
        print("Invalid format! Letters and numbers only.")
        time.sleep(1)
        continue

# converts letter into a column index
    col = ord(column_letter) - 65
    row = int(row_number)

# makes sure the guess is actually in range
    if row < 0 or row >= ROWS or col < 0 or col >= COLS:
        print("Out of range!")
        time.sleep(1)
        continue

# makes sure the player hasn't already guessed the cell
    if board[row][col] != " ":
        print("Already occupied or blocked!")
        time.sleep(1)
        continue

# places the checker
    board[row][col] = checker

# blocks the neighboring cells
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            # skip the center cell
            if dr == 0 and dc == 0:
                continue
            rr = row + dr
            cc = col + dc
            # if the neighbor is on the board and empty, block it
            if 0 <= rr < ROWS and 0 <= cc < COLS and board[rr][cc] == " ":
                board[rr][cc] = "#"

# checks to see if there are any empty cells left
    empty_cells = 0
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == " ":
                empty_cells = empty_cells + 1

# if there are no empty cells, end the game
    if empty_cells == 0:
        game_over = True
    else:
        # changes turn
        current_player = (current_player + 1) % NUM_PLAYERS
        time.sleep(1) # short pause before clearing screen for the next player





# clears the screen and shows the final board and win message 
os.system("clear")





# print the column letters one last time
print("   ", end="")
for c in range(COLS):
    print(chr(65 + c), end='   ')
print("\n  +" + "---+" * COLS)


# prints the row numbers and the cells of the board one last time
for r in range(ROWS):
    print(str(r) + " |", end="")
    for c in range(COLS):
        print(" " + board[r][c] + " |", end="")
    print("\n  +" + "---+" * COLS)

print("\nGAME OVER! Player " + str(current_player + 1) + " (" + checker + ") wins!")