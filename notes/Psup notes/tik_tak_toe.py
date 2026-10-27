board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]
current_player = "X"
moves = 0
game_over = False

print("Tic-Tac-Toe")
print("Enter a row and column from 1 to 3, separated by a space.")

while not game_over:
    print("\n  1 2 3")
    for row_number in range(3):
        print(f"{row_number + 1} {'|'.join(board[row_number])}")
        if row_number < 2:
            print("  -----")

    move = input(f"Player {current_player}, enter row and column: ").split()

    if len(move) != 2 or not move[0].isdigit() or not move[1].isdigit():
        print("Please enter two numbers, like: 2 3")
        continue

    row = int(move[0]) - 1
    column = int(move[1]) - 1

    if row < 0 or row > 2 or column < 0 or column > 2:
        print("Row and column must be between 1 and 3.")
        continue

    if board[row][column] != " ":
        print("That square is already taken. Choose another.")
        continue

    board[row][column] = current_player
    moves += 1

    won = False

    for index in range(3):
        if (
            board[index][0] == current_player
            and board[index][1] == current_player
            and board[index][2] == current_player
        ):
            won = True

        if (
            board[0][index] == current_player
            and board[1][index] == current_player
            and board[2][index] == current_player
        ):
            won = True

    if (
        board[0][0] == current_player
        and board[1][1] == current_player
        and board[2][2] == current_player
    ):
        won = True

    if (
        board[0][2] == current_player
        and board[1][1] == current_player
        and board[2][0] == current_player
    ):
        won = True

    if won:
        print("\n  1 2 3")
        for row_number in range(3):
            print(f"{row_number + 1} {'|'.join(board[row_number])}")
            if row_number < 2:
                print("  -----")
        print(f"Player {current_player} wins!")
        game_over = True
    elif moves == 9:
        print("\n  1 2 3")
        for row_number in range(3):
            print(f"{row_number + 1} {'|'.join(board[row_number])}")
            if row_number < 2:
                print("  -----")
        print("It's a draw!")
        game_over = True
    elif current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
