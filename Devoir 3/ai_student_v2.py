
ROW_COUNT = 6
COLUMN_COUNT = 7

def get_row(board, col):
    for r in range(ROW_COUNT):
        row = ROW_COUNT - r - 1
        if board[row][col] == 0:
            return row

def is_valid_move(board, move):
    if board[0][move] != 0:
        return False
    return True

def is_winning_move(board, player, move):
    row = get_row(board, move)
    # making the move 
    board[row][move] = player
    # checking if the move is a winning move
    if check_win(board, player):
        # undo the move 
        board[row][move] = 0
        return True
    # undo the move 
    board[row][move] = 0
    return False

def is_terminal_state(board):
    # checking if a player won
    if is_winning_move(board, 1) or is_winning_move(board, 2):
        return True 
    # checking if board is full
    for col in range(7):
        if board[0][col] == 0:
            return False
    return True

def check_win(board, player):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == player and board[r][c+1] == player and board[r][c+2] == player and board[r][c+3] == player:
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == player and board[r+1][c] == player and board[r+2][c] == player and board[r+3][c] == player:
                return True

    # Check positively sloped diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == player and board[r+1][c+1] == player and board[r+2][c+2] == player and board[r+3][c+3] == player:
                return True

    # Check negatively sloped diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == player and board[r-1][c+1] == player and board[r-2][c+2] == player and board[r-3][c+3] == player:
                return True

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

def evaluate_board(board, player):
    score = 0
    score += two_in_a_row(board, player)
    score += 10 * one_in_a_row(board, player)
    return score    

def ai_student_v2(board, player):
    opponent = 1 if player == 2 else 2
    # listing all the legit move
    legit_moves = [move for move in range(7) if is_valid_move(board, move)]
    # check if there is a winning move
    for move in legit_moves:
        if is_winning_move(board, player, move):
            return move
    # checking is there is a move that blocks the opponent from winning
    for move in legit_moves:
        if is_winning_move(board, opponent, move):
            return move
    # checking if there is a move that gives the player 3 in a row
    for move in legit_moves:
        board[get_row(board, move)][move] = player
        if three_in_a_row(board, player) > 0:
            board[get_row(board, move)][move] = 0
            return move
        board[get_row(board, move)][move] = 0
    # checking if there is a move that gives the opponent 3 in a row
    for move in legit_moves:
        board[get_row(board, move)][move] = opponent
        if three_in_a_row(board, opponent) > 0:
            board[get_row(board, move)][move] = 0
            return move
        board[get_row(board, move)][move] = 0
    # checking if there is a move that gives the player 2 in a row
    for move in legit_moves:
        board[get_row(board, move)][move] = player
        if two_in_a_row(board, player) > 0:
            board[get_row(board, move)][move] = 0
            return move
        board[get_row(board, move)][move] = 0
    # checking if there is a move that gives the opponent 2 in a row
    for move in legit_moves:
        board[get_row(board, move)][move] = opponent
        if two_in_a_row(board, opponent) > 0:
            board[get_row(board, move)][move] = 0
            return move
        board[get_row(board, move)][move] = 0
    return 0