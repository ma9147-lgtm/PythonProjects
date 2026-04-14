#import necessary modules
import random 
import os 


# variables that defines the rules of the game
SHIP_SIZE = 4 # constant variable for ship size
DIMENSION = 10 # constant variable for board size (square)
ROWS = 10
COLS = 10

# 2 10x10 boards
board = []
ship_board = []
for r in range(ROWS):
    board.append([" "] * COLS)
    ship_board.append([" "] * COLS)

#randomly choosing if ship is horizantal or vertical
orientation = random.randint(0,1)  

if orientation == 0:
    # placing horizantal ship
    ship_row = random.randint(0, ROWS-1)
    ship_col = random.randint(0, COLS-SHIP_SIZE)
    for i in range(SHIP_SIZE):
        ship_board[ship_row][ship_col+i] = "S"
else:
    # placing vertical ship
    ship_row = random.randint(0, ROWS-SHIP_SIZE)
    ship_col = random.randint(0, COLS-1)
    for i in range(SHIP_SIZE):
        ship_board[ship_row+i][ship_col] = "S"

# variables that keeps track of the player's progress
hits = 0
guesses = 0

# keep asking for the coordinates until the player gets 4 hits
while hits < SHIP_SIZE:
    os.system("clear")

# print the column letters (A-J)
    print("   ", end="")
    for c in range(COLS):
        print(chr(65 + c), end='   ')
    print("\n  +" + "---+" * COLS)

# prints the row numbers (1-9) and the cells of the board
    for r in range(ROWS):
        print(str(r) + " |", end="")
        for c in range(COLS):
            print(" " + board[r][c] + " |", end="")
        print("\n  +" + "---+" * COLS)

#user input
    guess = input("Enter coordinates (e.g. A5): ")

# checks if the input is too short   
    if len(guess) < 2:
        input("Invalid! Press Enter to try again.")
        continue

#split the input into the letter part and the number part
    column_letter = guess[0].upper() 
    row_number = guess[1:]


#makes sure the row is a number and the column is a letter
    if not row_number.isdigit() or not column_letter.isalpha():
        input("Invalid format! Press Enter.")
        continue

#converts letter into a column index
    col = ord(column_letter) - 65
    row = int(row_number)

#makes sure the guess is actually in range (0-9)
    if row < 0 or row >= ROWS or col < 0 or col >= COLS:
        input("Out of range! Press Enter.")
        continue

# makes sure the player hasn't already guessed the cell
    if board[row][col] == "X" or board[row][col] == "#":
        input("Already guessed! Press Enter.")
        continue

#increases guess count for new guesses
    guesses = guesses + 1

#checks the secret ship_board to see if it was a hit or a miss
    if ship_board[row][col] == "S":
        board[row][col] = "X"  #marks hit
        hits = hits + 1
        input("HIT! press enter")
    else:
        board[row][col] = "#" #marks miss
        input("MISS! Press Enter.")

#clears the screen anad shows the win message 
os.system("clear")
print("YOU SUNK THE SHIP!")
print("Final score: ", guesses)
