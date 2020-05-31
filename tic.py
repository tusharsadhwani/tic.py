"""Tic Tac Toe"""

x, o, blank = 'x', 'o', ' '

BOARD = '''
 {} | {} | {} 
-----------
 {} | {} | {} 
-----------
 {} | {} | {} 
'''


def print_board(board):
    """Prints the board to stdout"""
    print(BOARD.format(*board))


def player_input(char, board):
    """Takes position input from player"""
    pos = int(input(f'{char}>'))

    board[pos-1] = char


def check_win(char, board):
    """Checks if a player has won the game"""
    win = False

    rows = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
    )
    cols = (
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
    )
    diags = (
        (2, 4, 6),
        (0, 5, 8),
    )

    edges = (
        *rows,
        *cols,
        *diags
    )

    for edge in edges:
        if all([(board[i] == char) for i in edge]):
            win = True
            break

    return win


def check_tie(board):
    """Checks if the game was a tie"""
    return all([char != blank for char in board])


def turn(player, board):
    """Plays one turn of the game, and returns if the game has ended or not"""
    print_board(board)
    player_input(player, board)

    if check_win(player, board):
        print(f'Player {player} won!')
        print_board(board)
        return True

    if check_tie(board):
        print_board(board)
        print('It\'s a tie!')
        return True

    return False


def main():
    """Runs TicTacToe"""
    while True:
        input_string = input("Choose Player 1 symbol ('X' or 'O'): ")
        if not input_string:
            continue

        player_1 = input_string.strip()[0].lower()
        if player_1 == x:
            player_2 = o
            break

        if player_1 == o:
            player_2 = x
            break

        print('Try again')

    game_over = False
    board = [blank] * 9

    while not game_over:
        game_over = turn(player_1, board)
        game_over = turn(player_2, board)


if __name__ == '__main__':
    main()
