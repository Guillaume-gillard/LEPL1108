def evaluate_board(board, player):
    score = 0
    opponent = 3 - player
    # checking if winning move
    score += four_in_a_row(board, player)*100
    # checking if opponent has winning move
    score -= four_in_a_row(board, opponent)*100
    # checking if 3 in a row with space to win
    score += three_in_a_row(board, player)*50
    # checking if opponent has 3 in a row with space to win
    score -= three_in_a_row(board, opponent)*50
    # checking if 2 in a row with space to win 
    score += two_in_a_row(board, player)*10
    # checking if opponent has 2 in a row with space to win
    score -= two_in_a_row(board, opponent)*10
    # checking if 1 in a row with space to win
    score += one_in_a_row(board, player)*1
    # checking if opponent has 1 in a row with space to win
    score -= one_in_a_row(board, opponent)*1
    return score

def four_in_a_row(board, player):
    score = 0
    for col in range(7):
        for row in range(6):
            # checking horizontal
            if col+3 < 7:
                if board[row][col] == player and board[row][col+1] == player and board[row][col+2] == player and board[row][col+3] == player:
                    score += 1
            # checking vertical
            if row+3 < 6:
                if board[row][col] == player and board[row+1][col] == player and board[row+2][col] == player and board[row+3][col] == player:
                    score += 1
            # checking down left diag
            if col-3 >= 0 and row+3 < 6:
                if board[row][col] == player and board[row+1][col-1] == player and board[row+2][col-2] == player and board[row+3][col-3] == player:
                    score += 1
            # checking down right diag
            if col+3 < 7 and row+3 < 6:
                if board[row][col] == player and board[row+1][col+1] == player and board[row+2][col+2] == player and board[row+3][col+3] == player:
                    score += 1
    return score 

def three_in_a_row(board, player):
    score = 0
    for col in range(7):
        for row in range(6):
            # checking horizontal
            if col+3 < 7:
                if board[row][col] == player and board[row][col+1] == player and board[row][col+2] == player and board[row][col+3] == 0:
                    score += 1
            # checking vertical
            if row+3 < 6:
                if board[row][col] == player and board[row+1][col] == player and board[row+2][col] == player and board[row+3][col] == 0:
                    score += 1
            # checking down left diag
            if col-3 >= 0 and row+3 < 6:
                if board[row][col] == player and board[row+1][col-1] == player and board[row+2][col-2] == player and board[row+3][col-3] == 0:
                    score += 1
            # checking down right diag
            if col+3 < 7 and row+3 < 6:
                if board[row][col] == player and board[row+1][col+1] == player and board[row+2][col+2] == player and board[row+3][col+3] == 0:
                    score += 1
    return score 

def two_in_a_row(board, player):
    score = 0
    for col in range(7):
        for row in range(6):
            # checking horizontal
            if col+3 < 7:
                if board[row][col] == player and board[row][col+1] == player and board[row][col+2] == 0 and board[row][col+3] == 0:
                    score += 1
            # checking vertical
            if row+3 < 6:
                if board[row][col] == player and board[row+1][col] == player and board[row+2][col] == 0 and board[row+3][col] == 0:
                    score += 1
            # checking down left diag
            if col-3 >= 0 and row+3 < 6:
                if board[row][col] == player and board[row+1][col-1] == player and board[row+2][col-2] == 0 and board[row+3][col-3] == 0:
                    score += 1
            # checking down right diag
            if col+3 < 7 and row+3 < 6:
                if board[row][col] == player and board[row+1][col+1] == player and board[row+2][col+2] == 0 and board[row+3][col+3] == 0:
                    score += 1
    return score 

def one_in_a_row(board, player):
    score = 0
    for col in range(7):
        for row in range(6):
            # checking horizontal
            if col+3 < 7:
                if board[row][col] == player and board[row][col+1] == 0 and board[row][col+2] == 0 and board[row][col+3] == 0:
                    score += 1
            # checking vertical
            if row+3 < 6:
                if board[row][col] == player and board[row+1][col] == 0 and board[row+2][col] == 0 and board[row+3][col] == 0:
                    score += 1
            # checking down left diag
            if col-3 >= 0 and row+3 < 6:
                if board[row][col] == player and board[row+1][col-1] == 0 and board[row+2][col-2] == 0 and board[row+3][col-3] == 0:
                    score += 1
            # checking down right diag
            if col+3 < 7 and row+3 < 6:
                if board[row][col] == player and board[row+1][col+1] == 0 and board[row+2][col+2] == 0 and board[row+3][col+3] == 0:
                    score += 1
    return score 

def is_terminal_state(board):
    # checking if a player won
    if four_in_a_row(board, 1) or four_in_a_row(board, 2):
        return True 
    # checking if board is full
    for col in range(7):
        if board[0][col] == 0:
            return False
    return False

score_matrix = [0.8, 0.9, 1.0, 1.1, 1.0, 0.9, 0.8]

def minimax(board, player, depth, alpha, beta, maximizingPlayer):
    opponent = 3 - player
    if depth == 0 or is_terminal_state(board):
        return evaluate_board(board, player)
    if maximizingPlayer:
        value = -float('inf')
        for col in range(7):
            if is_valid_move(board, col):
                row = get_next_row(board, col)
                board[row][col] = player
                value = max(value, minimax(board, player, depth-1, alpha, beta, False))
                board[row][col] = 0
                alpha = max(alpha, value)
                if value >= beta:
                    break
        return value
    else:
        value = float('inf')
        for col in range(7):
            if is_valid_move(board, col):
                row = get_next_row(board, col)
                board[row][col] = opponent
                value = min(value, minimax(board, opponent, depth-1, alpha, beta, True))
                board[row][col] = 0
                beta = min(beta, value)
                if value <= alpha:
                    break
        return value

def get_next_row(board, col):
    for row in range(6):
        if board[5-row][col] == 0:
            return 5-row
    return None
        
def is_valid_move(board, col):
    return board[0][col] == 0

def ai_student(board, player):
    best_score = -float('inf')
    choosen_col = -1
    for col in range(7):
        if is_valid_move(board, col):
            row = get_next_row(board, col)
            board[row][col] = player
            score = minimax(board, player, 5, -float('inf'), float('inf'), False)
            board[row][col] = 0
            if score > best_score:
                best_score = score
                choosen_col = col
    return choosen_col
