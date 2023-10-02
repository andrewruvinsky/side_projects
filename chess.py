# Text-based Chess
# Created June 2023
# Written in Python, edited with Vim
# By Andrew Ruvinsky 
import os

def render_board(): # Constructs the chess board and displays pieces
    os.system('clear')
    rank = 8
    num = 0
    num2 = 0
    print('   ––––––––– ––––––––– ––––––––– ––––––––– ––––––––– ––––––––– ––––––––– –––––––––')
    for row in board:
        if num % 2 == 0:
            print('  |         |▓▓▓▓▓▓▓▓▓|         |▓▓▓▓▓▓▓▓▓|         |▓▓▓▓▓▓▓▓▓|         |▓▓▓▓▓▓▓▓▓|')
        else:
            print('  |▓▓▓▓▓▓▓▓▓|         |▓▓▓▓▓▓▓▓▓|         |▓▓▓▓▓▓▓▓▓|         |▓▓▓▓▓▓▓▓▓|         |')
        print(rank,end=' ')
        rank-=1
        for space in row:
            if num2 % 2 == 0:
                print('|    ' + space + '    ', end='')
            else:
                print('|▓▓▓ ' + space + ' ▓▓▓', end='')
            num2+=1
        print('|')
        if num % 2 == 0:
            print('  |         |▓▓▓▓▓▓▓▓▓|         |▓▓▓▓▓▓▓▓▓|         |▓▓▓▓▓▓▓▓▓|         |▓▓▓▓▓▓▓▓▓|')
        else:
            print('  |▓▓▓▓▓▓▓▓▓|         |▓▓▓▓▓▓▓▓▓|         |▓▓▓▓▓▓▓▓▓|         |▓▓▓▓▓▓▓▓▓|         |')
        num+=1
        num2+=1
        print('   ––––––––– ––––––––– ––––––––– ––––––––– ––––––––– ––––––––– ––––––––– –––––––––')
    print('       a         b         c         d         e         f         g         h    ')
# -------------------------------------------------------------------
def get_coords(loc): # Helper function that gets coordinates
    match loc[0]:
        case 'h':
            column=7
        case 'g':
            column=6
        case 'f':
            column=5
        case 'e':
            column=4
        case 'd':
            column=3
        case 'c':
            column=2
        case 'b':
            column=1
        case 'a':
            column=0

    row = 8 - int(loc[1])

    return row, column
# -------------------------------------------------------------------
def piece_rules(row1, column1, row2, column2): # Tells user if move is invalid based off the piece they're moving
    white_pieces = {'P', 'N', 'B', 'R', 'Q', 'K'} # ! Add detailed invalid move messages !
    black_pieces = {'p', 'n', 'b', 'r', 'q', 'k'}
    global piece
    piece = board[row1][column1]
    destination = board[row2][column2]
    delta_x = column2 - column1
    delta_y = row2 - row1

    if piece.lower() == 'p': # Pawn
        if is_white_turn: # White
            if row2 == row1 - 1 and column2 == column1 and destination == ' ':  # Move one square forward
                return row1, column1, row2, column2
            elif row2 == 4 and row1 == 6 and column1 == column2 and destination == ' ' and board[5][column1] == ' ': # Move 2 spcs
                return row1, column1, row2, column2
            elif row2 == row1 - 1 and abs(column2 - column1) == 1 and destination in black_pieces: # Capture
                return row1, column1, row2, column2
            else:
                render_board()
                print('Invalid move for pawn. Try again.')
                return False
        else: # Black
            if row2 == row1 + 1 and column2 == column1 and destination == ' ':  # Move one square forward
                return row1, column1, row2, column2
            elif row2 == 3 and row1 == 1 and column1 == column2 and destination == ' ' and board[2][column1] == ' ': # Move 2 spcs 
                return row1, column1, row2, column2
            elif row2 == row1 + 1 and abs(column2 - column1) == 1 and destination in white_pieces: # Capture
                return row1, column1, row2, column2
            else:
                render_board()
                print('Invalid move for pawn. Try again.')
                return False

    if piece.lower() == 'n': # Knight
        if is_white_turn: # White
            if abs(row2 - row1) == 2 and abs(column2 - column1) == 1 and destination not in white_pieces: # Move vertically
                return row1, column1, row2, column2
            elif abs(column2 - column1) == 2 and abs(row2 - row1) == 1 and destination not in white_pieces: # Move horizontally
                return row1, column1, row2, column2
            else:
                render_board()
                print('Invalid move for knight. Try again.')
                return False
        else: # Black
            if abs(row2 - row1) == 2 and abs(column2 - column1) == 1 and destination not in black_pieces: # Move vertically
                return row1, column1, row2, column2
            elif abs(column2 - column1) == 2 and abs(row2 - row1) == 1 and destination not in black_pieces: # Move horizontally
                return row1, column1, row2, column2
            else:
                render_board()
                print('Invalid move for knight. Try again.')
                return False

    if piece.lower() == 'b': # Bishop
        if delta_x == 0 or delta_y == 0:    # Prevents division by zero error which crashes program
            render_board()
            print('Invalid move for bishop. Try again.')
            return False
        x_step = int(delta_x / abs(delta_x))
        y_step = int(delta_y / abs(delta_y))

        if is_white_turn: # White
            if abs(delta_x) is abs(delta_y) and destination not in white_pieces: # Checks if path is diagonal and that destination
                for i in range(1, abs(delta_x)):                                 # isn't on a white piece
                    if board[row1 + (y_step * i)][column1 + (x_step * i)] != ' ': # If at any point the program notices a non-empty 
                        render_board()                                   # square along the diagonal path the bishop is trying
                        print('Bishop blocked! Try again.')          # to travel, it returns False and exits the function.
                        return False

                return row1, column1, row2, column2

            else:
                render_board()
                print('Invalid move for bishop. Try again.')
                return False

        else: # Black
            if abs(delta_x) is abs(delta_y) and destination not in black_pieces: 
                for i in range(1, abs(delta_x)):
                    if board[row1 + (y_step * i)][column1 + (x_step * i)] != ' ': 
                        render_board()
                        print('Bishop blocked! Try again.')
                        return False

                return row1, column1, row2, column2

            else:
                render_board()
                print('Invalid move for bishop. Try again.')
                return False

    if piece.lower() == 'r': # Rook
        if delta_y == 0:
            y_step = 0
            x_step = int(delta_x / abs(delta_x))
        else:
            x_step = 0
            y_step = int(delta_y / abs(delta_y))
        if is_white_turn: # White
            if destination not in white_pieces and ((delta_y != 0 and delta_x == 0) or (delta_y == 0 and delta_x != 0)):
                for i in range(1, abs(delta_y + delta_x)):
                    if board[row1 + (y_step * i)][column1 + (x_step * i)] != ' ':
                        render_board()
                        print('Rook blocked!')
                        return False
                return row1, column1, row2, column2

            else:
                render_board()
                print('Invalid move for rook. Try again!')
                return False

        else: # Black
            if destination not in black_pieces and ((delta_y != 0 and delta_x == 0) or (delta_y == 0 and delta_x != 0)):
                for i in range(1, abs(delta_y + delta_x)):
                    if board[row1 + (y_step * i)][column1 + (x_step * i)] != ' ':
                        render_board()
                        print('Rook blocked!')
                        return False
                return row1, column1, row2, column2

            else:
                render_board()
                print('Invalid move for rook. Try again!')
                return False

    if piece.lower() == 'q': # Queen
        if is_white_turn: # White           vvv If the queen moves like a rook, here are the rules: 
            if destination not in white_pieces and ((delta_y != 0 and delta_x == 0) or (delta_y == 0 and delta_x != 0)):
                if delta_y == 0:
                    y_step = 0
                    x_step = int(delta_x / abs(delta_x))
                else:
                    x_step = 0
                    y_step = int(delta_y / abs(delta_y))

                for i in range(1, abs(delta_y + delta_x)):
                    if board[row1 + (y_step * i)][column1 + (x_step * i)] != ' ':
                        render_board()
                        print('Queen blocked!')
                        return False
                return row1, column1, row2, column2
            # vvv If the queen moves like a bishop, here are the rules
            elif destination not in white_pieces and abs(delta_x) is abs(delta_y):
                if delta_x == 0:    # Prevents division by zero error which crashes program
                    render_board()
                    print('Invalid move for queen. Try again.')
                    return False
                x_step = int(delta_x / abs(delta_x))
                y_step = int(delta_y / abs(delta_y))
                for i in range(1, abs(delta_x)):                                 
                    if board[row1 + (y_step * i)][column1 + (x_step * i)] != ' ': 
                        render_board()
                        print('Queen blocked! Try again.') 
                        return False

                return row1, column1, row2, column2


            else: #      vvv If the queen moves like neither a rook or bishop, then return False
                render_board()
                print('Invalid move for queen. Try again!')
                return False
        else: # Black           vvv If the queen moves like a rook, here are the rules: 
            if destination not in black_pieces and ((delta_y != 0 and delta_x == 0) or (delta_y == 0 and delta_x != 0)):
                if delta_y == 0:
                    y_step = 0
                    x_step = int(delta_x / abs(delta_x))
                else:
                    x_step = 0
                    y_step = int(delta_y / abs(delta_y))

                for i in range(1, abs(delta_y + delta_x)):
                    if board[row1 + (y_step * i)][column1 + (x_step * i)] != ' ':
                        render_board()
                        print('Queen blocked!')
                        return False
                return row1, column1, row2, column2
            # vvv If the queen moves like a bishop, here are the rules
            elif destination not in black_pieces and abs(delta_x) is abs(delta_y):
                if delta_x == 0:    # Prevents division by zero error which crashes program
                    render_board()
                    print('Invalid move for queen. Try again.')
                    return False
                x_step = int(delta_x / abs(delta_x))
                y_step = int(delta_y / abs(delta_y))
                for i in range(1, abs(delta_x)):                                 
                    if board[row1 + (y_step * i)][column1 + (x_step * i)] != ' ': 
                        render_board()
                        print('Queen blocked! Try again.') 
                        return False

                return row1, column1, row2, column2
            else: #      vvv If the queen moves like neither a rook or bishop, then return False
                render_board()
                print('Invalid move for queen. Try again.')
                return False

    if piece.lower() == 'k': # King
        if is_white_turn: # White
            if destination not in white_pieces and (abs(delta_x) in range(1,2) or abs(delta_y) in range(1,2)):
                return row1, column1, row2, column2
            else:
                render_board()
                print('Invalid move for king. Try again.')
                return False
        else: # Black
            if destination not in black_pieces and (abs(delta_x) in range(1,2) or abs(delta_y) in range(1,2)):
                return row1, column1, row2, column2
            else:
                render_board()
                print('Invalid move for king. Try again.')
                return False


            # -------------------------------------------------------------------
def check_move(move, is_white_turn):       # Parses input from the user
    global white_qs_castle
    global white_ks_castle
    global black_qs_castle
    global black_ks_castle
    if len(move) == 5 and \
            move[0] in {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'} and \
            move[1] in {'1','2','3','4','5','6','7','8'} and \
            move[2] == ' ' and \
            move[3] in {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'} and \
            move[4] in {'1','2','3','4','5','6','7','8'}:
                loc1 = move[0]+move[1]
                loc2 = move[3]+move[4]
                row1, column1 = get_coords(loc1) # Calling helper function here...
                row2, column2 = get_coords(loc2) # ...and here
                piece = board[row1][column1]

                if piece == ' ':
                    render_board()
                    print('You selected an empty space, please choose a space with a piece.')
                    return False
                elif is_white_turn == True and piece in {'p','n','b','r','q','k'}:
                    render_board()
                    print('White, you can\'t move black\'s pieces!')
                    return False
                elif is_white_turn == False and piece in {'P','N','B','R','Q','K'}:
                    render_board()
                    print('Black, you can\'t move white\'s pieces!')
                    return False
                elif piece_rules(row1, column1, row2, column2) == False:
                    return False
                elif is_white_turn and loc1 == 'a1': # Checks if white's queen's rook has moved
                    white_qs_castle = False
                    return row1, column1, row2, column2
                elif is_white_turn and loc1 == 'h1': # Checks if white's king's rook has moved
                    white_ks_castle = False
                    return row1, column1, row2, column2
                elif is_white_turn and loc1 == 'e1':
                    white_qs_castle = False
                    white_ks_castle = False
                    return row1, column1, row2, column2
                elif is_white_turn and loc1 == 'e8':
                    white_qs_castle = False
                    white_ks_castle = False
                    return row1, column1, row2, column2
                elif is_white_turn == False and loc1 == 'a8': # Checks if black's queen's rook has moved
                    black_qs_castle = False
                    return row1, column1, row2, column2
                elif is_white_turn == False and loc1 == 'h8': # Checks if black's king's rook has moved
                    black_ks_castle = False
                    return row1, column1, row2, column2
                else:
                    return row1, column1, row2, column2

    elif move == 'O-O-O':
        y = 7 if is_white_turn else 0
        if board[y][0].lower() == 'r' and board[y][1] == ' ' and board[y][2] == ' ' and board[y][3] == ' ' and board[y][4].lower() == 'k':
            if is_white_turn and white_qs_castle:
                return True
            elif is_white_turn == False and black_qs_castle:
                return True
            else:
                render_board()
                print('Rook or king have moved, unable to castle queenside.')
        else:
            render_board()
            print('Unable to castle queenside, pieces in wrong positions.')

    elif move == 'O-O':
        y = 7 if is_white_turn else 0
        if board[y][4].lower() == 'k' and board[y][5] == ' ' and board[y][6] == ' ' and board[y][7].lower() == 'r':
            if is_white_turn and white_ks_castle:
                return True
            elif is_white_turn == False and black_ks_castle:
                return True
            else:
                render_board()
                print('Rook or king have moved, unable to castle kingside.')
        else:
            render_board()
            print('Unable to castle kingside, pieces in wrong positions.')

    elif move.lower() == 'quit': # Quit program
        exit()
    else:
        render_board()
        print('Invalid syntax, try again. (e.g. e2 e4)')
    return False
# -------------------------------------------------------------------
def promote_pawn(promotion, row2, column2):
    if is_white_turn:
        board[row2][column2] = promotion.upper()
    else:
        board[row2][column2] = promotion.lower()
# -------------------------------------------------------------------
def castle(move):
    if is_white_turn:
        if move == 'O-O-O':
            board[7][2] = 'K'
            board[7][4] = ' '
            board[7][3] = 'R'
            board[7][0] = ' '
        elif move == 'O-O':
            board[7][4] = ' '
            board[7][5] = 'R'
            board[7][6] = 'K'
            board[7][7] = ' '
    else:
        if move == 'O-O-O':
            board[0][2] = 'k'
            board[0][4] = ' '
            board[0][3] = 'r'
            board[0][0] = ' '
        elif move == 'O-O':
            board[0][4] = ' '
            board[0][5] = 'r'
            board[0][6] = 'k'
            board[0][7] = ' '
# -------------------------------------------------------------------
def move_piece(row1, column1, row2, column2):
    piece = board[row1][column1]
    board[row1][column1] = ' '

    board[row2][column2] = piece
# -------------------------------------------------------------------
def start_screen():
    os.system('clear')
    print('\n\n\n')
    print('Welcome! This program runs a human vs human text-based chess game locally on this device.')
    print('Disclaimer: This is not a chess engine')
    print()
    print('Each piece is represented on the board as their first initial (P for pawn, K for king).')
    print('This applies for all pieces besides the knight which is represented by N.')
    print('White\'s pieces are capitalized. Black\'s pieces are lowercase.')
    print()
    print('In order to move a piece, you must select its point on the grid by entering...')
    print('the coordinates for both the piece you want to move and its destination.')
    print('When inputting a move, you must follow the proper syntax:')
    print('         a-h 1-8     a-h 1-8')
    print('          1   2   3   4   5')
    print('Example input: e2 e4')
    print('To castle queenside, type \'O-O-O\'. To castle kingside, type \'O-O\'.')
    print('En passant is not supported in this version.')
    print('Type \'quit\' at any time to exit the program.')
    print('\n\n\n\n\n\n\n')
    key = input('     ENTER ANY KEY TO CONTINUE OR TYPE QUIT TO EXIT PROGRAM\n\n\n\n\n\n\n')
    if key.lower() == 'quit':
        exit()
    else:
        return
# -------------------------------------------------------------------
checkmate = False
white_qs_castle = True
white_ks_castle = True
black_qs_castle = True
black_ks_castle = True
is_white_turn = True
board = [
        ['r','n','b','q','k','b','n','r'], # 8
        ['p','p','p','p','p','p','p','p'], # 7
        [' ',' ',' ',' ',' ',' ',' ',' '], # 6
        [' ',' ',' ',' ',' ',' ',' ',' '], # 5
        [' ',' ',' ',' ',' ',' ',' ',' '], # 4
        [' ',' ',' ',' ',' ',' ',' ',' '], # 3
        ['P','P','P','P','P','P','P','P'], # 2
        ['R','N','B','Q','K','B','N','R']  # 1
        ]
#         a   b   c   d   e   f   g   h

start_screen()
while checkmate == False:
    render_board()
    if is_white_turn == True:           # If it is white's turn, print 'White to move. '
        move = input('White to move. ')
    else:
        move = input('Black to move. ') # If it is black's turn, print 'Black to move. '
    while check_move(move, is_white_turn) == False: # Allow user to re-enter their move until check_move(...) returns True
        if is_white_turn == True:
            move = input('White to move. ')
        else:
            move = input('Black to move. ')
    if move in {'O-O-O', 'O-O'}:
        castle(move)
    else:
        row1, column1, row2, column2 = check_move(move, is_white_turn) # Getting coordinates from check_move function...
        move_piece(row1, column1, row2, column2)  # Plugging those coordinates into move_piece(...)
        y = 0 if is_white_turn else 7
        if piece.lower() == 'p' and row2 == y:
            render_board()
            promotion = input('Promote your pawn! Type Q for queen, R for rook, B for bishop, and N for knight.\n')
            while promotion.lower() not in {'q','r','b','n'}:
                render_board()
                promotion = input('Try again. Promote your pawn by choosing from one of the four pieces (Q, R, B, N).\n')
            promote_pawn(promotion, row2, column2)

    if is_white_turn == True:           # If it was just white's turn, set is_white_turn False
        is_white_turn = False
    else:
        is_white_turn = True            # If it was just black's turn, set is_white_turn True
