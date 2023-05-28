import random
#Taher Farg Code ***********************************************************************************************

board = [' ' for x in range(9)]

human = 'X'
computer = 'O'


winning_combinations = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
]


def print_board():
    print('-------------')
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('-------------')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('-------------')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('-------------')


def is_board_full(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def check_winner(board, player):
    for combination in winning_combinations:
        if board[combination[0]] == player and board[combination[1]] == player and board[combination[2]] == player:
            return True
    return False


def computer_move():
    
    for i in range(9):
        if board[i] == ' ':
            board[i] = computer
            if check_winner(board, computer):
                return i
            else:
                board[i] = ' '

    
    for i in range(9):
        if board[i] == ' ':
            board[i] = human
            if check_winner(board, human):
                board[i] = computer
                return i
            else:
                board[i] = ' '

    corners = [0, 2, 6, 8]
    available_corners = []
    for i in corners:
        if board[i] == ' ':
            available_corners.append(i)
    if len(available_corners) > 0:
        return random.choice(available_corners)

    
    if board[4] == ' ':
        return 4

    edges = [1, 3, 5, 7]
    available_edges = []
    for i in edges:
        if board[i] == ' ':
            available_edges.append(i)
    if len(available_edges) > 0:
        return random.choice(available_edges)


def human_move():
    while True:
        move = input('Enter your move (1-9): ')
        try:
            move = int(move) - 1
            if move >= 0 and move <= 8:
                if board[move] == ' ':
                    board[move] = human
                    return
                else:
                    print('That space is already taken.')
            else:
                print('Please enter a number between 1 and 9.')
        except ValueError:
            print('Please enter a number between 1 and 9.')

# Define the function for the Minimax algorithm ***************************************************************************************************
def minimax(board, depth, is_maximizing):
    if check_winner(board, computer):
        return 1
    elif check_winner(board, human):
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -1000
        for i in range(9):
            if board[i] == ' ':
                board[i] = computer
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                if score > best_score:
                    best_score = score
        return best_score
    else:
        best_score = 1000
        for i in range(9):
            if board[i] == ' ':
                board[i] = human
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                if score < best_score:
                    best_score = score
        return best_score
def main():
    print_board()

    while not is_board_full(board):
        if not check_winner(board, computer):
            human_move()
            print_board()
        else:
            print('Sorry, you lost! Nobe!')
            break

        if not check_winner(board, human):
            move = computer_move()
            board[move] = computer
            print('Computer placed an \'O\' in position', move + 1, ':')
            print_board()
        else:
            print('Congratulations, you won!')
            break

    if is_board_full(board) and not check_winner(board, human) and not check_winner(board, computer):
        print('It\'s a tie!')

while True:
    choice = input('Do you want to play With Me ? (y/n): ')
    if choice.lower() == 'y':
        board = [' ' for x in range(9)]
        print('-----------------------------------')
        main()
    else:
        break