import random
import os
def display_board(board):
    clear_screen() # Clears the screen
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("Player 1, choose X or O: ").upper()
        if marker not in ['X', 'O']:
            print("Invalid input, choose either X or O")
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, marker):
    return ((board[1] == board[2] == board[3] == marker) or
            (board[4] == board[5] == board[6] == marker) or
            (board[7] == board[8] == board[9] == marker) or
            (board[1] == board[4] == board[7] == marker) or
            (board[2] == board[5] == board[8] == marker) or
            (board[3] == board[6] == board[9] == marker) or
            (board[1] == board[5] == board[9] == marker) or
            (board[3] == board[5] == board[7] == marker))

def choose_first():
    flip = random.randint(1, 2)
    if flip == 1:
        return 'player 1'
    else:
        return 'player 2'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        try:
            position = int(input("Choose your next position (1-9): "))
            if position not in range(1, 10):
                print("Invalid input, choose a position between 1 and 9.")
        except ValueError:
            print("Invalid input, please enter a number.")
    return position

def replay():
    choice = input("Play again? Enter Yes or No: ").lower()
    return choice == 'yes'

# MAIN FUNCTION
print("Welcome to TIC TAC TOE")

while True:
    board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + " will go first")

    play_game = input('Ready to play? y or n: ').lower()
    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'player 1':
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)

            if win_check(board, player1_marker):
                display_board(board)
                print("Player 1 has WON!!")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("TIE Game!!")
                    break
                else:
                    turn = 'player 2'

        else:
            display_board(board)
            position = player_choice(board)
            place_marker(board, player2_marker, position)

            if win_check(board, player2_marker):
                display_board(board)
                print("Player 2 has WON!!")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("TIE Game!!")
                    break
                else:
                    turn = 'player 1'

    if not replay():
        break
