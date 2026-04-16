import random

ROWS = 20
COLS = 10
CELL_SIZE = 20

BOARD_WIDTH = COLS * CELL_SIZE
BOARD_HEIGHT = ROWS * CELL_SIZE

COLOR_OPTIONS = [
    (255, 51, 52),    # red
    (12, 150, 228),   # blue
    (30, 183, 66),    # green
    (246, 187, 0),    # yellow
    (76, 0, 153),     # purple
    (255, 255, 255),  # white
    (0, 0, 0)         # black
]

game = None


class Block:
    def __init__(self, row, col, block_color):
        self.__row = row
        self.__col = col
        self.__color = block_color

    # getters
    def get_row(self):
        return self.__row

    def get_col(self):
        return self.__col

    def get_color(self):
        return self.__color

    # setters
    def set_row(self, row):
        self.__row = row

    def set_col(self, col):
        self.__col = col

    def set_color(self, block_color):
        self.__color = block_color

    # movement methods
    def move_down(self):
        self.__row += 1

    def move_left(self):
        self.__col -= 1

    def move_right(self):
        self.__col += 1

    def same_color(self, other):
        if other is None:
            return False
        return self.__color == other.get_color()

    def display(self):
        fill(self.__color[0], self.__color[1], self.__color[2])
        noStroke()
        rect(self.__col * CELL_SIZE, self.__row * CELL_SIZE, CELL_SIZE, CELL_SIZE)

    def __str__(self):
        return "Block(" + str(self.__row) + ", " + str(self.__col) + ", " + str(self.__color) + ")"


class Game:
    def __init__(self):
        self.reset_game()

    def reset_game(self):
        self.__board = []
        for r in range(ROWS):
            row_list = []
            for c in range(COLS):
                row_list.append(None)
            self.__board.append(row_list)

        self.__current_block = None
        self.__score = 0
        self.__speed = 0
        self.__game_over = False
        self.__just_spawned = False

        self.spawn_new_block(False)

    # getters
    def get_score(self):
        return self.__score

    def get_speed(self):
        return self.__speed

    def get_game_over(self):
        return self.__game_over

    def get_current_block(self):
        return self.__current_block

    def __str__(self):
        return "Game(score=" + str(self.__score) + ", speed=" + str(self.__speed) + ")"

    def spawn_new_block(self, increase_speed=True):
        available_columns = []

        for c in range(COLS):
            if self.__board[0][c] is None:
                available_columns.append(c)

        if len(available_columns) == 0:
            self.__current_block = None
            self.__game_over = True
            return

        new_col = random.choice(available_columns)
        new_color = random.choice(COLOR_OPTIONS)

        self.__current_block = Block(0, new_col, new_color)
        self.__just_spawned = True

        if increase_speed:
            self.__speed += 0.25

    def can_move_down(self):
        if self.__current_block is None:
            return False

        row = self.__current_block.get_row()
        col = self.__current_block.get_col()

        next_row = row + 1

        if next_row >= ROWS:
            return False

        if self.__board[next_row][col] is not None:
            return False

        return True

    def move_block_left(self):
        if self.__game_over or self.__current_block is None:
            return

        row = self.__current_block.get_row()
        col = self.__current_block.get_col()
        new_col = col - 1

        if new_col < 0:
            return

        if self.__board[row][new_col] is not None:
            return

        self.__current_block.move_left()

    def move_block_right(self):
        if self.__game_over or self.__current_block is None:
            return

        row = self.__current_block.get_row()
        col = self.__current_block.get_col()
        new_col = col + 1

        if new_col >= COLS:
            return

        if self.__board[row][new_col] is not None:
            return

        self.__current_block.move_right()

    def place_current_block(self):
        if self.__current_block is None:
            return

        row = self.__current_block.get_row()
        col = self.__current_block.get_col()

        self.__board[row][col] = self.__current_block
        self.__current_block = None

        groups_removed = self.check_vertical_groups(col)

        if groups_removed > 0:
            self.__score += groups_removed
            self.__speed = 0

        self.spawn_new_block(True)

    def check_vertical_groups(self, col):
        removed_groups = 0
        found_match = True

        while found_match:
            found_match = False

            for start_row in range(ROWS - 3):
                b1 = self.__board[start_row][col]
                b2 = self.__board[start_row + 1][col]
                b3 = self.__board[start_row + 2][col]
                b4 = self.__board[start_row + 3][col]

                if b1 is not None and b2 is not None and b3 is not None and b4 is not None:
                    if b1.same_color(b2) and b2.same_color(b3) and b3.same_color(b4):
                        self.__board[start_row][col] = None
                        self.__board[start_row + 1][col] = None
                        self.__board[start_row + 2][col] = None
                        self.__board[start_row + 3][col] = None

                        removed_groups += 1
                        found_match = True
                        break

        return removed_groups

    def update(self):
        if self.__game_over or self.__current_block is None:
            return

        if self.__just_spawned:
            self.__just_spawned = False
            return

        if self.can_move_down():
            self.__current_block.move_down()
        else:
            self.place_current_block()

    def draw_grid(self):
        stroke(180)

        for x in range(0, BOARD_WIDTH + 1, CELL_SIZE):
            line(x, 0, x, BOARD_HEIGHT)

        for y in range(0, BOARD_HEIGHT + 1, CELL_SIZE):
            line(0, y, BOARD_WIDTH, y)

    def draw_blocks(self):
        for r in range(ROWS):
            for c in range(COLS):
                if self.__board[r][c] is not None:
                    self.__board[r][c].display()

        if self.__current_block is not None and not self.__game_over:
            self.__current_block.display()

    def draw_hud(self):
        fill(0)
        textSize(15)

        textAlign(LEFT, TOP)
        text("Speed: " + str(round(self.__speed, 2)), 5, 5)

        textAlign(RIGHT, TOP)
        text("Score: " + str(self.__score), width - 5, 5)

    def draw_game_over(self):
        fill(0)
        textAlign(CENTER, CENTER)

        textSize(22)
        text("Game over", width / 2, height / 2 - 20)

        textSize(16)
        text("Final Score: " + str(self.__score), width / 2, height / 2 + 5)
        text("Click to restart", width / 2, height / 2 + 28)

    def display(self):
        if not self.__game_over:
            self.update()

        self.draw_blocks()
        self.draw_grid()
        self.draw_hud()

        if self.__game_over:
            self.draw_game_over()


def setup():
    global game
    size(BOARD_WIDTH, BOARD_HEIGHT)
    game = Game()


def draw():
    if frameCount % (max(1, int(8 - game.get_speed()))) == 0 or frameCount == 1:
        background(210)
        game.display()


def keyPressed():
    if game.get_game_over():
        return

    if keyCode == LEFT:
        game.move_block_left()
    elif keyCode == RIGHT:
        game.move_block_right()


def mousePressed():
    if game.get_game_over():
        game.reset_game()
