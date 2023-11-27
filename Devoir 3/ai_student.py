import random 

ROW_COUNT = 6
COLUMN_COUNT = 7

database = {}

def is_valid_move(board, col):
    if board[0][col] != 0:
        return False
    return True

def get_row(board, col):
    for r in range(ROW_COUNT):
        row = ROW_COUNT - r - 1
        if board[row][col] == 0:
            return row
        
def is_winning_move(board, player, move):
    row = get_row(board, move)
    board[row][move] = player
    if check_win(board, player):
        # undo the move 
        board[row][move] = 0
        return True
    # undo the move 
    board[row][move] = 0
    return False

def check_win(board, player):
    # Check horizontal 
    for col in range(COLUMN_COUNT):
        for row in range(ROW_COUNT):
            if col+3 < 7:  
                if board[row][col] == player and board[row][col+1] == player and board[row][col+2] == player and board[row][col+3] == player:
                    return True

            # Check vertical
            if row+3 < 6:
                if board[row][col] == player and board[row+1][col] == player and board[row+2][col] == player and board[row+3][col] == player:
                    return True

            # Check down right diagonals
            if col+3 < 7 and row+3 < 6:
                if board[row][col] == player and board[row+1][col+1] == player and board[row+2][col+2] == player and board[row+3][col+3] == player:
                    return True

            # Check down left diagonals
            if col-3 >= 0 and row+3 < 6:
                if board[row][col] == player and board[row+1][col-1] == player and board[row+2][col-2] == player and board[row+3][col-3] == player:
                    return True

def evaluate_board(board, player):
    score = 0
    opponent = 1 if player == 2 else 2
    for i in range(four_in_a_row(board, player)):
        score += 1000
    for i in range(four_in_a_row(board, opponent)):
        score -= 1000
    for i in range(three_in_a_row(board, player)):
        score += 50
    for i in range(two_in_a_row(board, player)):
        score += 10
    for i in range(one_in_a_row(board, player)):
        score += 1
    for i in range(three_in_a_row(board, opponent)):
        score -= 50
    for i in range(two_in_a_row(board, opponent)):
        score -= 10
    for i in range(one_in_a_row(board, opponent)):
        score -= 1
    return score    

def four_in_a_row(board, player):
    # Check horizontal 
    score = 0
    for col in range(COLUMN_COUNT):
        for row in range(ROW_COUNT):
            if col+3 < 7:  
                if board[row][col] == player and board[row][col+1] == player and board[row][col+2] == player and board[row][col+3] == player:
                    score += 1

            # Check vertical
            if row+3 < 6:
                if board[row][col] == player and board[row+1][col] == player and board[row+2][col] == player and board[row+3][col] == player:
                    score += 1

            # Check down right diagonals
            if col+3 < 7 and row+3 < 6:
                if board[row][col] == player and board[row+1][col+1] == player and board[row+2][col+2] == player and board[row+3][col+3] == player:
                    score += 1

            # Check down left diagonals
            if col-3 >= 0 and row+3 < 6:
                if board[row][col] == player and board[row+1][col-1] == player and board[row+2][col-2] == player and board[row+3][col-3] == player:
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
    return True

score_matrix = [0.2, 0.5, 1.0, 3, 1.0, 0.5, 0.2]

def minimax(board, player, depth, alpha, beta, maximizingPlayer):
    opponent = 1 if player == 2 else 2
    if depth == 0 or is_terminal_state(board):
        #print("terminal state")
        return evaluate_board(board, player)
    
    if maximizingPlayer:
        value = -float('inf')
        for col in range(7):
            if is_valid_move(board, col):
                row = get_row(board, col)
                board[row][col] = player
                value = max(value, minimax(board, opponent, depth-1, alpha, beta, False)*score_matrix[col])
                #print("maximizing value: ", value)
                alpha = max(alpha, value)
                board[row][col] = 0  
                if value >= beta:
                    break     
        #database[str(board)] = value
        return value
    else:
        value = float('inf')
        for col in range(7):
            if is_valid_move(board, col):
                row = get_row(board, col)
                board[row][col] = opponent
                value = min(value, minimax(board, player, depth-1, alpha, beta, True)*score_matrix[col])
                #print("minimizing value: ", value)
                beta = min(beta, value)
                board[row][col] = 0  
                if value <= alpha:
                    break
        #database[str(board)] = value
        return value

def ai_student(board, player):
    #print("AI turn :))")
    opponent = 1 if player == 2 else 2
    # listing all the legit move
    legit_moves = [col for col in range(7) if is_valid_move(board, col)]
    random.shuffle(legit_moves)  # Shuffle for random move selection among equally good moves
    best_score = -float('inf')
    chosen_col = -1
    for col in legit_moves:
        row = get_row(board, col)
        board[row][col] = player
        score = minimax(board, player, 3, -float('inf'), float('inf'), False)
        board[row][col] = 0
        #print(f'Move at col {col} with score {score}')
        if score > best_score:
            best_score = score
            chosen_col = col

    #print('Chosen col: ', chosen_col, ' with score: ', best_score)
    return chosen_col

""""
60 pourcent de win rate contre random
"""