import pygame
import sys
from ai_student import ai_student
import numpy as np
import math

# Define constants
ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARE_SIZE = 100
WIDTH = COLUMN_COUNT * SQUARE_SIZE
HEIGHT = (ROW_COUNT + 1) * SQUARE_SIZE  # Extra row for the header

# Define colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Initialize Pygame
pygame.init()

# Create the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the title of the window
pygame.display.set_caption("Connect Four")

# Function to create the board
def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

# Function to draw the board
def draw_board(board):
    for row in range(ROW_COUNT):
        for col in range(COLUMN_COUNT):
            pygame.draw.rect(window, BLUE, (col * SQUARE_SIZE, (row + 1) * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.circle(window, BLACK, (col * SQUARE_SIZE + SQUARE_SIZE // 2, (row + 1) * SQUARE_SIZE + SQUARE_SIZE // 2), 40)

    for row in range(ROW_COUNT):
        for col in range(COLUMN_COUNT):
            if board[row][col] == 1:
                pygame.draw.circle(window, RED, (col * SQUARE_SIZE + SQUARE_SIZE // 2, (row + 1) * SQUARE_SIZE + SQUARE_SIZE // 2), 40)
            elif board[row][col] == 2:
                pygame.draw.circle(window, YELLOW, (col * SQUARE_SIZE + SQUARE_SIZE // 2, (row + 1) * SQUARE_SIZE + SQUARE_SIZE // 2), 40)

# Function to drop a piece into the board
def drop_piece(board, row, col, piece):
    board[row][col] = piece

# Function to check if a column is valid for dropping a piece
def is_valid_location(board, col):
    return board[0][col] == 0

# Function to find the next available row in a column
def get_next_open_row(board, col):
    for r in range(ROW_COUNT - 1, -1, -1):
        if board[r][col] == 0:
            return r

# Function to check for a win
def winning_move(board, piece):
    # Check horizontal
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                return True

    # Check vertical
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                return True

    # Check positively sloped diagonal
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                return True

    # Check negatively sloped diagonal
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                return True

    return False

def print_board(board):
    for row in range(ROW_COUNT):
        print(board[row])

board = create_board()
#print_board(board)
game_over = False
turn = 0

pygame.init()

SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE/2 - 5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)

        if event.type == pygame.MOUSEBUTTONDOWN and turn == 0:  # Player's turn
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            posx = event.pos[0]
            col = int(math.floor(posx/SQUARESIZE))

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 1)

                draw_board(board)
                pygame.display.update()  # Update display after player's move

                if winning_move(board, 1):
                    label = myfont.render("You win!!", 1, RED)
                    screen.blit(label, (40, 10))
                    pygame.display.update()
                    pygame.time.wait(2000)  # Delay for 2000 milliseconds (2 seconds) before exiting
                    game_over = True

                turn = 1  # Switch to AI's turn

        # AI's turn
        if turn == 1 and not game_over:
            col = ai_student(board, 2)

            if is_valid_location(board, col):
                pygame.time.wait(50)
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 2)

                draw_board(board)
                pygame.display.update()  # Update display after AI's move

                if winning_move(board, 2):
                    label = myfont.render("AI wins!!", 1, YELLOW)
                    screen.blit(label, (40, 10))
                    pygame.display.update()
                    pygame.time.wait(2000)  # Delay for 2000 milliseconds (2 seconds) before exiting
                    game_over = True

                turn = 0  # Switch to player's turn

    draw_board(board)
    pygame.display.update()