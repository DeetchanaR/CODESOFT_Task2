board = [" " for _ in range(9)]

def print_board():
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def print_positions():
    print("\nChoose positions as:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print()


def check_winner(board, player):
    win_patterns = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for pattern in win_patterns:
        if all(board[i] == player for i in pattern):
            return True

    return False


def is_draw(board):
    return " " not in board


def minimax(board, is_maximizing):

    if check_winner(board, "O"):
        return 1

    if check_winner(board, "X"):
        return -1

    if is_draw(board):
        return 0

    if is_maximizing:

        best_score = -float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = " "
                best_score = max(score, best_score)

        return best_score

    else:

        best_score = float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = " "
                best_score = min(score, best_score)

        return best_score


def ai_move():

    best_score = -float("inf")
    best_move = None

    for i in range(9):

        if board[i] == " ":

            board[i] = "O"

            score = minimax(board, False)

            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"


def human_move():

    while True:

        try:
            move = int(input("Enter your move (1-9): ")) - 1

            if move < 0 or move > 8:
                print("Please enter a number between 1 and 9.")
                continue

            if board[move] != " ":
                print("Position already occupied!")
                continue

            board[move] = "X"
            break

        except ValueError:
            print("Please enter a valid number.")


print("=" * 40)
print("      TIC-TAC-TOE AI")
print("=" * 40)

print_positions()

while True:

    print_board()

    human_move()

    if check_winner(board, "X"):
        print_board()
        print("🎉 Congratulations! You Win!")
        break

    if is_draw(board):
        print_board()
        print("🤝 It's a Draw!")
        break

    print("AI is thinking...\n")

    ai_move()

    if check_winner(board, "O"):
        print_board()
        print("🤖 AI Wins!")
        break

    if is_draw(board):
        print_board()
        print("🤝 It's a Draw!")
        break
