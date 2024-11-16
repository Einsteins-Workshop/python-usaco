winner = '='
turn = 1
board = [None,'[]','[]','[]','[]','[]','[]','[]','[]','[]']

print('GameStart')
while winner == '=':
    for i in range(1, 10,3):
        print(board[i],board[i+1],board[i+2])
    if turn == 1:
        mark = int(input('Player1:'))
        if mark == 1:
            board[1] = '[x]'
        elif mark == 2:
            board[2] = '[x]'
        elif mark == 3:
            board[3] = '[x]'
        elif mark == 4:
            board[4] = '[x]'
        elif mark == 5:
            board[5] = '[x]'
        elif mark == 6:
            board[6] = '[x]'
        elif mark == 7:
            board[7] = '[x]'
        elif mark == 8:
            board[8] = '[x]'
        elif mark == 9:
            board[9] = '[x]'
        turn = 2
    else:
        mark = int(input('Player2:'))
        if mark == 1:
            board[1] = '[o]'
        elif mark == 2:
            board[2] = '[o]'
        elif mark == 3:
            board[3] = '[o]'
        elif mark == 4:
            board[4] = '[o]'
        elif mark == 5:
            board[5] = '[o]'
        elif mark == 6:
            board[6] = '[o]'
        elif mark == 7:
            board[7] = '[o]'
        elif mark == 8:
            board[8] = '[o]'
        elif mark == 9:
            board[9] = '[o]'
        turn = 1
    if board[1] == '[x]' and board[2] == '[x]' and board[3] == '[x]':
        winner = 'x'
    elif board[4] == '[x]' and board[5] == '[x]' and board[6] == '[x]':
        winner = 'x'
    elif board[7] == '[x]' and board[7] == '[x]' and board[9] == '[x]':
        winner = 'x'
    elif board[1] == '[x]' and board[4] == '[x]' and board[7] == '[x]':
        winner = 'x'
    elif board[2] == '[x]' and board[5] == '[x]' and board[8] == '[x]':
        winner = 'x'
    elif board[3] == '[x]' and board[6] == '[x]' and board[9] == '[x]':
        winner = 'x'
    elif board[1] == '[x]' and board[5] == '[x]' and board[9] == '[x]':
        winner = 'x'
    elif board[3] == '[x]' and board[5] == '[x]' and board[7] == '[x]':
        winner = 'x'

    if board[1] == '[o]' and board[2] == '[o]' and board[3] == '[o]':
        winner = 'o'
    elif board[4] == '[o]' and board[5] == '[o]' and board[6] == '[o]':
        winner = 'o'
    elif board[7] == '[o]' and board[8] == '[o]' and board[9] == '[o]':
        winner = 'o'
    elif board[1] == '[o]' and board[4] == '[o]' and board[7] == '[o]':
        winner = 'o'
    elif board[2] == '[o]' and board[5] == '[o]' and board[8] == '[o]':
        winner = 'o'
    elif board[3] == '[o]' and board[6] == '[o]' and board[9] == '[o]':
        winner = 'o'
    elif board[1] == '[o]' and board[5] == '[o]' and board[9] == '[o]':
        winner = 'o'
    elif board[3] == '[o]' and board[5] == '[o]' and board[7] == '[o]':
        winner = 'o'
    if board[1] != '[]' and board[2] != '[]' and board[3] != '[]' and board[4] != '[]' and board[5] != '[]' and board[6] != '[]' and board[7] != '[]' and board[8] != '[]' and board[9] != '[]' and winner == '=':
        winner = '-'
    if winner == '-':
        print(board[1],   board[2], board[3])
        print(board[4], board[5], board[6])
        print(board[7], board[8], board[9])
        print('GameOver')
        print('Draw')
    if winner != '=' and winner != '-':
        print(board[1], board[2], board[3])
        print(board[4], board[5], board[6])
        print(board[7], board[8], board[9])
        print('GameOver')
        if winner == 'x':
            print('Player1 wins!')
        else:
            print('Player2 wins!')
# hello