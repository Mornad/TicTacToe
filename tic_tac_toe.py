
def validate(choice, choice_list):
    return len(choice) == 1 and choice in choice_list

def validate_and_move(cell, sign, board):
    choice_list = ('1', '2', '3', '4', '5', '6', '7', '8','9')
    if validate(cell, choice_list) and \
            board[int(cell) - 1] == ' ':
        board[int(cell) - 1] = sign
        return True
    else:
        return False

def print_board(board):
    print(f'''
     {board[6]} | {board[7]} | {board[8]} 
    ---|---|---
     {board[3]} | {board[4]} | {board[5]} 
    ---|---|---
     {board[0]} | {board[1]} | {board[2]} \n''')

def check_win(board, sign):
    if sign == board[0] == board[3] == board[6] or \
        sign == board[1] == board[4] == board[7] or \
        sign == board[2] == board[5] == board[8] or \
        sign == board[0] == board[1] == board[2] or \
        sign == board[3] == board[4] == board[5] or \
        sign == board[6] == board[7] == board[8] or \
        sign == board[0] == board[4] == board[8] or \
        sign == board[2] == board[4] == board[6]:
        return True
    else:
        return False

def announce_and_score(sign, players, scores):
    scores[players[sign] - 1] += 1
    print(f'Player{players[sign]} won!')

def ask():
    choice = ''
    while True:
        choice = input('Play again? Y,N: ')
        if validate(choice, ['Y', 'N']):
            break
    return choice

def move(sign, players, board):
    while True:
        move = input(f'Player{players[sign]} move: ')
        if validate_and_move(move, sign, board):
            break
        else:
            print('Illegal move')

    print_board(board)

playing = True

print('''
Here is the board, in order to place your sign, input
the relevant cell number!

 7 | 8 | 9 
---|---|---
 4 | 5 | 6 
---|---|---
 1 | 2 | 3 ''')

choice = ''
while True:
    choice = input('Do you want to play? Y,N: ')
    if validate(choice, ['Y', 'N']):
        break

if choice == 'N':
    playing = False

scores = [0, 0]

while playing:
    players = {'X': 1, 'O': 2}
    board = [' '] * 9
    print(f'Scores are: Player1: {scores[0]} Player2: {scores[1]}')
    while playing:
        player1 = input('Please choose X or O. X goes first.'
                        ' Player1 is: ')
        valid_sign = validate(player1, ['X', 'O'])
        if valid_sign:
            if player1 == 'O':
                players['O'] = 1
                players['X'] = 2
                break
            else:
                break
        else:
            print('Invalid sign chosen')

    while playing:
        last_move = ''

        move('X', players, board)

        if check_win(board, 'X'):
            announce_and_score('X', players, scores)
            if ask() =='N':
                playing = False
            break
        elif ' ' not in board:
            print('Tie!')
            if ask() == 'N':
                playing = False
            break

        move('O', players, board)

        if check_win(board, 'O'):
            announce_and_score('O', players, scores)
            if ask() == 'N':
                playing = False
            break






