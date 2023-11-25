def evaluate_board(board, player):
    score = 0
    opponent = 3 - player
    # checking if winning move
    score += is_winning_move(board, player)*100
    # checking if opponent has winning move
    score -= is_winning_move(board, opponent)*100
    # checking if 2 in a row with space to win 
    score += two_in_a_row(board, player)*10
    # checking if opponent has 2 in a row with space to win
    score -= two_in_a_row(board, opponent)*10
    # checking if 1 in a row with space to win
    score += one_in_a_row(board, player)*1
    # checking if opponent has 1 in a row with space to win
    score -= one_in_a_row(board, opponent)*1
    return score

def is_winning_move(board, player):
    score = 0
    for col in range(7):
        for row in range(6):
            # checking horizontal
            if col < 4:
                if board[row][col] == player and board[row][col+1] == player and board[row][col+2] == player and board[row][col+3] == player and board[row][col+4] == 0:
                    score += 1
            # checking vertical
            if row-3 >= 0:
                if board[row][col] == player and board[row+1][col] == player and board[row+2][col] == player and board[row+3][col] == player and board[row+4][col] == 0:
                    score += 1
            # checking down left diag 
            if col > 2 and row < 3:
                if board[row][col] == player and board[row-1][col-1] == player and board[row-2][col-2] == player and board[row-3][col-3] == player and board[row-4][col-4] == 0:
                    score += 1
            # checking down right diag
            if col < 4 and row < 3:
                if board[row][col] == player and board[row-1][col+1] == player and board[row-2][col+2] == player and board[row-3][col+3] == player and board[row-4][col+4] == 0:
                    score += 1
    return score 

def is_terminal_state(board):
    # checking if board is full
    for col in range(7):
        if board[0][col] == 0:
            return False
    # checking if a player won
    if check_win(board, 1) or check_win(board, 2):
        return True 
    return False

def check_win(board, player):
    for col in range(7):
            for row in range(6):
                # checking horizontal
                if col < 4:
                    if board[row][col] == player and board[row][col+1] == player and board[row][col+2] == player:
                        return True
                # checking vertical
                if row < 3:
                    if board[row][col] == player and board[row+1][col] == player and board[row+2][col] == player:
                        return True
                # checking down left diag
                if col > 2 and row < 3:
                    if board[row][col] == player and board[row-1][col-1] == player and board[row-2][col-2] == player:
                        return True
                # checking down right diag
                if col < 4 and row < 3:
                    if board[row][col] == player and board[row-1][col+1] == player and board[row-2][col+2] == player:
                        return True
    return False 

def two_in_a_row(board, player):
    score = 0
    for col in range(7):
        for row in range(6):
            # checking horizontal
            if col < 4:
                if board[row][col] == player and board[row][col+1] == player and board[row][col+2] == 0:
                    score += 1
            # checking vertical
            if row < 3:
                if board[row][col] == player and board[row+1][col] == player and board[row+2][col] == 0:
                    score += 1
            # checking down left diag
            if col > 2 and row < 3:
                if board[row][col] == player and board[row-1][col-1] == player and board[row-2][col-2] == 0:
                    score += 1
            # checking down right diag
            if col+4 < 7 and row-4 >= 0:
                if board[row][col] == player and board[row-1][col+1] == player and board[row-2][col+2] == 0:
                    score += 1
    return score 


def one_in_a_row(board, player):
    score = 0
    for col in range(7):
        for row in range(6):
            # checking horizontal
            if col < 4:
                if board[row][col] == player and board[row][col+1] == 0:
                    score += 1
            # checking vertical
            if row < 3:
                if board[row][col] == player and board[row+1][col] == 0:
                    score += 1
            # checking down left diag
            if col > 2 and row < 3:
                if board[row][col] == player and board[row-1][col-1] == 0:
                    score += 1
            # checking down right diag
            if col < 4 and row < 3:
                if board[row][col] == player and board[row-1][col+1] == 0:
                    score += 1
    return score

def minimax(board, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or is_terminal_state(board):
        return evaluate_board(board, 1)
    if maximizingPlayer:
        maxEval = -float('inf')
        for col in range(7):
            if is_valid_move(board, col):
                row = get_next_row(board, col)
                board[row][col] = 1
                eval = minimax(board, depth - 1, alpha, beta, False)
                board[row][col] = 0
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return maxEval
    else:
        minEval = float('inf')
        for col in range(7):
            if is_valid_move(board, col):
                row = get_next_row(board, col)
                board[row][col] = 2
                eval = minimax(board, depth - 1, alpha, beta, True)
                board[row][col] = 0
                minEval = min(minEval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return minEval

def get_next_row(board, col):
    for row in range(6):
        if board[5-row][col] == 0:
            return 5-row
        
def is_valid_move(board, col):
    return board[0][col] == 0

def ai_student(board, player):
    best_score = -float('inf')
    choosen_col = None
    for col in range(7):
        if is_valid_move(board, col):
            row = get_next_row(board, col)
            board[row][col] = player
            score = minimax(board, 4, -float('inf'), float('inf'), False)
            board[row][col] = 0
            if score > best_score:
                best_score = score
                choosen_col = col
    return choosen_col-3
