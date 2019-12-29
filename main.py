import sys
import pygame

pygame.init()
# create game window
screen = pygame.display.set_mode((930, 930))
# Title and Icon
pygame.display.set_caption("Sudoku Solver")  # title
icon = pygame.image.load("sudoku.png")
pygame.display.set_icon(icon)
# dimensions for each rectangle in the 9x9 grid
width = 100
height = 100
margin = 3
# colors
white = (255, 255, 255)
blue = (0, 100, 200)
black = (0, 0, 0)
# create font for numbers and intro text
number_font = pygame.font.Font('ChunkFive-Regular.otf', 60)
intro_font = pygame.font.Font('Corbert-Regular.otf', 30)
# some self-explanatory variables
user_choosing_num = False
chosen_box_x = 0
chosen_box_y = 0
# create 2-D arrays to store numbers
storednums = []
for row in range(9):
    storednums.append([0, 0, 0, 0, 0, 0, 0, 0, 0])


def draw_rectangle(x, y, color):
    """Draws rectagles onto the screen."""
    global screen
    global margin
    global width
    global height
    pygame.draw.rect(screen, color, [((margin + width) * x + margin),
                                     ((margin + height) * y + margin),
                                     width, height])


def show_numbers(num, x, y):
    """Draws numbers onto the screen."""
    global number_font
    num_text = number_font.render(num, True, black)
    screen.blit(num_text, (x, y))


# functions for solving algorithm
def find_empty(board):
    """Return rows and columns (respectively) of some empty square."""
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)


def isValid(board, num, pos):
    """Return whether or not the given num is valid at some position on the board."""
    # Check row
    for i in range(len(board[0])):
        # Loops through every column in a row and checks if the value is present and thus invalid
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    # Check column
    for i in range(len(board)):
        # Loops through every row and checks if the column value is the same for any position
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    # Check 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    # Multiply values by 3 (box index 2 has index 6)
    for i in range(box_y * 3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    # returns true if all checks satisfied
    return True


def solve(board):
<<<<<<< HEAD:sudokusolver/main.py
    """
    Recursive implementation of solving the board.
    """
=======
    '''
    Recursive implementation of solving the board
    '''
>>>>>>> b79ae167a80e407e465801000cc6e67c9821f373:PygameBootcamp/SudokuSolver/main.py
    global margin
    # base case - the end of the board has been reached by the algorithm
    # i.e no more empty squares
    find = find_empty(board)
    if not find:
        return True
    else:
        # assign variables to row, column in tuple returned from find_empty()
        row, col = find

    for i in range(1, 10):
        # if valid, add to board
        if isValid(board, i, (row, col)):
            board[row][col] = i
            # recursively call solve with the updated board until solution is found
            if solve(board):
                return True
            # backtrack and reset the board state to the last step
            board[row][col] = 0

    return False


# ----------------------------- INTRO LOOP ---------------------------------------------
intro_running = True
while intro_running:
    screen.fill(white)
    intro_text = ["Hello! This is a sudoku puzzle solver.",
<<<<<<< HEAD:sudokusolver/main.py
                  "Sudoku is played on a 9x9 board with numbers 1-9",
                  "where the rules are as follows:",
                  "1.  No number may appear in the same row twice.",
                  "2. No number may appear in the same column twice.",
                  "3. No number may appear in the same 3x3 square.",
                  # "   marked by thicker lines on the board.", <-- WIP feature
                  "",
                  "Instructions:",
                  "Click a square and type a number to add it to the board.",
                  "Press SPACE to solve the puzzle and R to reset the board.",
                  "Press SPACE to begin!"]
=======
    "Sudoku is played on a 9x9 board with numbers 1-9",
    "where the rules are as follows:",
    "1.  No number may appear in the same row twice.",
    "2. No number may appear in the same column twice.",
    "3. No number may appear in the same 3x3 square.",
    # "   marked by thicker lines on the board.", <-- WIP feature
    "",
    "Instructions:",
    "Click a square and type a number to add it to the board.",
    "Press SPACE to solve the puzzle and R to reset the board.",
    "Press SPACE to begin!"]
>>>>>>> b79ae167a80e407e465801000cc6e67c9821f373:PygameBootcamp/SudokuSolver/main.py
    label = []
    for line in intro_text:
        label.append(intro_font.render(line, True, black))
    for line in range(len(label)):
        screen.blit(label[line], (10, 50 + 50 * line))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                intro_running = False

    pygame.display.update()

# ----------------------------- MAIN LOOP --------------------------------------------
running = True
while running:
    screen.fill(black)
    # create grid
    for row in range(9):
        for column in range(9):
            # actual grid
            draw_rectangle(row, column, white)
            # turns squares blue when chosen
            if user_choosing_num is True:
                draw_rectangle(chosen_box_x, chosen_box_y, blue)
            # adds numbers (if the code on this line looks stupid to you, it does to me as well: it just centers each number)
            if storednums[column][row] != 0:
                show_numbers(str(storednums[column][row]), row*100 + 40 + margin*row, column*100 + 20 + margin*column)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # let user enter numbers
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            chosen_box_x = (position[0] // 100)
            chosen_box_y = (position[1] // 100)
            draw_rectangle(chosen_box_x, chosen_box_y, blue)
            user_choosing_num = True
        # updates list of numbers with the user's input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1 and user_choosing_num is True:
                storednums[chosen_box_y][chosen_box_x] = 1
                user_choosing_num = False

            if event.key == pygame.K_2 and user_choosing_num is True:
                storednums[chosen_box_y][chosen_box_x] = 2
                user_choosing_num = False

            if event.key == pygame.K_3 and user_choosing_num is True:
                storednums[chosen_box_y][chosen_box_x] = 3
                user_choosing_num = False

            if event.key == pygame.K_4 and user_choosing_num is True:
                storednums[chosen_box_y][chosen_box_x] = 4
                user_choosing_num = False

            if event.key == pygame.K_5 and user_choosing_num is True:
                storednums[chosen_box_y][chosen_box_x] = 5
                user_choosing_num = False

            if event.key == pygame.K_6 and user_choosing_num is True:
                storednums[chosen_box_y][chosen_box_x] = 6
                user_choosing_num = False

            if event.key == pygame.K_7 and user_choosing_num is True:
                storednums[chosen_box_y][chosen_box_x] = 7
                user_choosing_num = False

            if event.key == pygame.K_8 and user_choosing_num is True:
                storednums[chosen_box_y][chosen_box_x] = 8
                user_choosing_num = False

            if event.key == pygame.K_9 and user_choosing_num is True:
                storednums[chosen_box_y][chosen_box_x] = 9
                user_choosing_num = False

            if event.key == pygame.K_0 and user_choosing_num is True:
                storednums[chosen_box_y][chosen_box_x] = 0
                user_choosing_num = False

            # shortcut to reset the board:
            if event.key == pygame.K_r:
                storednums = []
                for i in range(9):
                    storednums.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
            # Solve the puzzle
            if event.key == pygame.K_SPACE:
                # algorithm: there must be no duplicate numbers on each row/column, and in each squares
                # use backtracking (notes for self: upon invalid case, backtracking means to go back to the PREVIOUS step)
                # --> the program will continue to go backwards until a new valid solution is found,
                #     reducing the overall computations massively compared to a more naive method
                solve(storednums)
                if storednums[column][row] != 0:
                    show_numbers(str(storednums[column][row]), row*100 + 40 + margin*row, column*100 + 20 + margin*column)

    pygame.display.update()
