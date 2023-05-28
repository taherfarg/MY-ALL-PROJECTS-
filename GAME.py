import math
import random
import pygame
import numpy as np

# Set up the board and initialize the game
board = np.zeros((3,3), dtype=int)
player = 1
game_over = False
game_result = None

# Initialize Pygame
pygame.init()
WIDTH = 400
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Define the font for the messages
font = pygame.font.Font(None, 32)

# Draw the game board
def draw_board():
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, (0, i*HEIGHT/3), (WIDTH, i*HEIGHT/3), 3)
        pygame.draw.line(screen, BLACK, (i*WIDTH/3, 0), (i*WIDTH/3, HEIGHT), 3)

# Get the available moves on the board
def get_available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                moves.append((i, j))
    return moves

# Check if the game is over
def is_game_over(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            return True, board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != 0:
            return True, board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return True, board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return True, board[0][2]
    if len(get_available_moves(board)) == 0:
        return True, None
    return False, None

# Evaluate the score of the board state
def evaluate_board(board):
    score = 0
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == 1:
                score += 10
            elif board[i][0] == -1:
                score -= 10
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == 1:
                score += 10
            elif board[0][i] == -1:
                score -= 10
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 1:
            score += 10
        elif board[0][0] == -1:
            score -= 10
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 1:
            score += 10
        elif board[0][2] == -1:
            score -= 10
    return score

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    game_over, winner = is_game_over(board)
    if game_over:
        if winner == 1:
            return None, 100 - depth
        elif winner == -1:
            return None, -100 + depth
        else:
            return None, 0
    if is_maximizing:
        best_score = -math.inf
        best_move = None
        for move in get_available_moves(board):
            board[move[0]][move[1]] = 1
            score = minimax(board, depth+1, False)[1]
            board[move[0]][move[1]] = 0
            if score > best_score:
                best_score = score
                best_move = move
        return best_move, best_score
    else:
        best_score = math.inf
        best_move = None
        for move in get_available_moves(board):
            board[move[0]][move[1]] = -1
            score = minimax(board, depth+1, True)[1]
            board[move[0]][move[1]] = 0
            if score < best_score:
                best_score = score
                best_move = move
        return best_move, best_score
    
# Main game loop
while True:
    # Check if the game is over
    game_over, winner = is_game_over(board)
    if game_over:
        if winner == 1:
            game_result = "Player 1 wins!"
        elif winner == -1:
            game_result = "Player 2 wins!"
        else:
            game_result = "Tie!"
    
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            if player == 1:
                x, y = pygame.mouse.get_pos()
                row = int(y // (HEIGHT/3))
                col = int(x // (WIDTH/3))
                if board[row][col] == 0:
                    board[row][col] = player
                    player *= -1
            else:
                move = minimax(board, 0, True)[0]
                board[move[0]][move[1]] = player
                player *= -1
    
    # Draw the board
    screen.fill(WHITE)
    draw_board()
    
    # Draw the players
    for i in range(3):
        for j in range(3):
            if board[i][j] == 1:
                pygame.draw.circle(screen, RED, (int(j*WIDTH/3 + WIDTH/6), int(i*HEIGHT/3 + HEIGHT/6)), 40, 3)
            elif board[i][j] == -1:
                pygame.draw.line(screen, BLUE, (j*WIDTH/3 + 20, i*HEIGHT/3 + HEIGHT/3 - 20), (j*WIDTH/3 + WIDTH/3 - 20, i*HEIGHT/3 + 20), 3)
                pygame.draw.line(screen, BLUE, (j*WIDTH/3 + 20, i*HEIGHT/3 + 20), (j*WIDTH/3 + WIDTH/3 - 20, i*HEIGHT/3 + HEIGHT/3 - 20), 3)
    
    # Display the game result
    if game_result is not None:
        text = font.render(game_result, True, BLACK)
        text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
        screen.blit(text, text_rect)
    
    # Update the display
    pygame.display.update()
    
    
    
