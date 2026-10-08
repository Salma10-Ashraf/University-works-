board = [" " for _ in range(9)]

def print_board(b):
    for i in range(0, 9, 3):
        print(b[i], "|", b[i+1], "|", b[i+2])
    print("-" * 10)

def check_winner(b, player):
    win_positions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for pos in win_positions:
        if all(b[i] == player for i in pos):
            return True
    return False

def is_draw(b):
    return " " not in b

def minimax(b, is_max):
    if check_winner(b, "X"):
        return 1
    if check_winner(b, "O"):
        return -1
    if is_draw(b):
        return 0

    if is_max:
        best = -float("inf")
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, False)
                b[i] = " "
                best = max(best, score)
        return best
    else:
        best = float("inf")
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, True)
                b[i] = " "
                best = min(best, score)
        return best

def best_move(b):
    best_score = -float("inf")
    move = -1
    for i in range(9):
        if b[i] == " ":
            b[i] = "X"
            score = minimax(b, False)
            b[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

board[0] = "X"
board[4] = "O"

print_board(board)
print(best_move(board))