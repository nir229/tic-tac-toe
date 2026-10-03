def print_board(board):
    """
    Get a printout of the Tic-Tac-Toe board.
    :param board: list
    :return: None
    """
    num_row = 0
    for row in board:
        num_row += 1
        print(" | ".join(row))
        if num_row <= 2:
            print("-" * 12)


def full_board(board):
    """
    Check if the game board is full.
    :param board: list
    :return: boolean True/False
    """
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "  ":
                return False
    return True

def game(number, name):
    """
    Checks and updates the board based on the player's choice, including verifying whether the selected spot is already occupied.
    :param number: number
    :param name: string user1/user2
    :return: None
    """
    global number_of_play

    match number:
        case 1 | 2 | 3:
            index = 0
        case 4 | 5 | 6:
            index = 1
        case 7 | 8 | 9:
            index = 2

    match number:
        case 1 | 4 | 7:
            num = 0
        case 2 | 5 | 8:
            num = 1
        case 3 | 6 | 9:
            num = 2

    if name == user1:
        if board[index][num] == "  ":
            board[index][num] = "X"
            number_of_play += 1
        else:
            print("That spot is taken \nplease choose a new number.")
    if name == user2:
        if board[index][num] == "  ":
            board[index][num] = "O"
            number_of_play += 1
        else:
            print("That spot is taken \nplease choose a new number.")


def win(board, sign_play):
    """
    Checking for a game win
    :param board: list
    :param sign_play: string X or O
    :return: boolean True/False
    """
    for line in board:
        if line[0] == sign_play and line[1] == sign_play and line[2] == sign_play:
            return True
    for i in range(3):
        if board[0][i] == sign_play and board[1][i] == sign_play and board[2][i] == sign_play:
            return True
    if board[0][0] == sign_play and board[1][1] == sign_play and board[2][2] == sign_play:
        return True
    if board[0][2] == sign_play and board[1][1] == sign_play and board[2][0] == sign_play:
        return True
    return False


while True:

    user1 = input("Please enter your name \nyou are play whit X: ")
    print()
    user2 = input("Please enter your name \nyou are play whit O: ")

    board = [
        ["  ", "  ", "  "],
        ["  ", "  ", "  "],
        ["  ", "  ", "  "],
    ]

    number_of_play = 1

    while True:
        if win(board, sign_play= "X"):
            print(f"The winner is {user1} 😎🏆")
            break
        if win(board, sign_play= "O"):
            print(f"The winner is {user2} 😎🏆")
            break
        if full_board(board):
            print("The game is over in even")
            break

        input_user = input("Please enter a number between 1 and 9: ")

        if not input_user.isdigit():
            print("Enter a valid number")
            continue

        if int(input_user) < 1 or int(input_user) > 9:
            print("Enter a number between 1 and 9")
            continue

        if number_of_play % 2 == 0:
            game(int(input_user), user2)
        else:
            game(int(input_user), user1)


        print()
        print_board(board)
        print()

    print()
    play_again = input("Would you like to play again? (y/n): ")
    if play_again.lower() == "y":
        continue
    else:
        print("Goodbye!\nThank you for playing")
        break