from random import random
from time import sleep
import os
from colorama import init, Fore

init()


def random_state(board_height, board_width):
    """Takes two arguments which define the size of the board and returns a
    board where every cell has been randomly assigned either
    1 (alive) or 0 (dead)."""
    return [[random_generator() for cell in range(board_width)]
            for cell in range(board_height)]


def random_generator():
    """Generates a random number and returns either 1 or 0
    depending on the frequency assigned"""
    random_number = random()
    # Frequency of returning 1 is set to %50.
    if random_number > 0.5:
        return 1
    else:
        return 0


def dead_state(board_height, board_width):
    """Takes two arguments which define the size of the board and returns a
    board where every cell is set to 0 (dead)"""
    return [[0 for cells in range(board_width)]
            for cells in range(board_height)]


def print_board(board):
    """Takes a board and prints it to the console with a border.
    If a cell is 1 (alive) two green blocks are printed, if a cell is
    0 (dead) '  ' is printed instead."""
    result = []
    for lines in board:
        result_line = ''
        for pixel in lines:
            # If the pixel is alive two green blocks are added to the line.
            if pixel == 1:
                result_line += Fore.GREEN + u"\u2593\u2593"
            else:
                result_line += '  '
        result.append(result_line)

    # Underscores are printed at the top and bottom of the board.
    top_and_bottom = '__'
    top_and_bottom += '_' * (2 * len(lines))

    print('  ' + top_and_bottom)

    for line in result:
        print(' | ' + line + Fore.RESET + ' |')

    print(' |' + top_and_bottom + '|')


def next_board_state(initial_board):
    """Receives an initial board, calculates the next board and returns it."""
    board = dead_state(len(initial_board), len(initial_board[0]))
    for h, line in enumerate(initial_board):
        for w, cell in enumerate(line):
            # Find the number of living cells within the area of each cell.
            living_neighbours = check_neighbours(initial_board, h, w)
            if cell == 1:
                # Number_alive includes the current cell so is removed.
                living_neighbours -= 1
                if living_neighbours < 2:
                    # Cell dies because there are too few neighbours.
                    board[h][w] = 0
                elif living_neighbours > 3:
                    # Cell dies because there are too many neighbours.
                    board[h][w] = 0
                elif living_neighbours == 2 or 3:
                    # Cell lives because there are either 2 or 3 neighbours.
                    board[h][w] = 1
            else:
                # Dead cell only changes if there are 3 neighbouring cells.
                if living_neighbours == 3:
                    # New cell is created because of breading.
                    board[h][w] = 1
    return board


def check_neighbours(initial_board, y, x):
    """Takes a board and coordinates and checks 9 cells in the area for alive
    status. Returns the number of alive cells in the area."""
    number_alive = 0
    area_to_check = []
    for index, lines in enumerate(range(0, 3)):
        line_to_check = []
        for pixel, columns in enumerate(range(0, 3)):
            # Negative coordinates are not checked.
            if index + y != 0 and pixel + x != 0:
                line_to_check.append([index + (y - 1), pixel + (x - 1)])

        area_to_check.append(line_to_check)

    for line in area_to_check:
        for co_ords in line:
            # Coordinates higher than the size of the board are not checked.
            if co_ords[0] <= (height - 1):
                if co_ords[1] <= (width - 1):
                    if initial_board[co_ords[0]][co_ords[1]] == 1:
                        number_alive += 1
    return number_alive


def load_board(file):
    """Opens the file with the name given and returns a set of integers in a
    nested list."""
    with open(file, 'r') as file:
        text = [lines.strip() for lines in file.readlines()]

    return [[int(cell) for cell in line] for line in text]


def gol_menu():
    """Asks the user to choose an option, then loads and returns the selected
    board."""
    in_menu = True
    while in_menu:
        os.system('cls')
        print("\n\t[1] Random board")
        print("\t[2] Toad")
        print("\t[3] Beacon")
        print("\t[4] Blinker")
        print("\t[5] Glider")
        print("\t[6] Gosper Glider Gun")
        print("\t[7] Penta Decathlon")
        print("\t[8] Pulsar")
        user_choice = input("\t Please choose one of the above options: ")

        if user_choice == '1':
            user_board = random_state(height, width)
            return user_board, len(user_board), len(user_board[0])

        elif user_choice == '2':
            user_board = load_board('toad.txt')
            return user_board, len(user_board), len(user_board[0])

        elif user_choice == '3':
            user_board = load_board('beacon.txt')
            return user_board, len(user_board), len(user_board[0])

        elif user_choice == '4':
            user_board = load_board('blinker.txt')
            return user_board, len(user_board), len(user_board[0])

        elif user_choice == '5':
            user_board = load_board('glider.txt')
            return user_board, len(user_board), len(user_board[0])

        elif user_choice == '6':
            user_board = load_board('gosper_glider_gun.txt')
            return user_board, len(user_board), len(user_board[0])

        elif user_choice == '7':
            user_board = load_board('penta.txt')
            return user_board, len(user_board), len(user_board[0])

        elif user_choice == '8':
            user_board = load_board('pulsar.txt')
            return user_board, len(user_board), len(user_board[0])

        else:
            print("\tSorry I don't understand that.")
            sleep(2)


height = 40
width = 110

current_board, height, width = gol_menu()

running = True

while running:
    os.system('cls')

    print_board(current_board)

    next_board = next_board_state(current_board)

    current_board = next_board

    sleep(0.2)
