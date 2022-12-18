'''
                       /$$             /$$     /$$       /$$                   /$$  
                      | $$            | $$    | $$      |__/                 /$$$$  
 /$$$$$$$   /$$$$$$  /$$$$$$         /$$$$$$  | $$$$$$$  /$$  /$$$$$$$      |_  $$  
| $$__  $$ /$$__  $$|_  $$_/        |_  $$_/  | $$__  $$| $$ /$$_____/        | $$  
| $$  \ $$| $$  \ $$  | $$            | $$    | $$  \ $$| $$|  $$$$$$         | $$  
| $$  | $$| $$  | $$  | $$ /$$        | $$ /$$| $$  | $$| $$ \____  $$        | $$  
| $$  | $$|  $$$$$$/  |  $$$$/        |  $$$$/| $$  | $$| $$ /$$$$$$$/       /$$$$$$
|__/  |__/ \______/    \___/           \___/  |__/  |__/|__/|_______/       |______/                                                                                
                                                                                    
'''


import pprint as PP
from itertools import chain

X = 900
Y = 900

INIT_Y = Y//2
INIT_X = X//2

def read_data(filename):
    data = []
    f = open(filename, "r")
    for l in f:
        if l.strip():
            data.append(tuple(l.split()))
    f.close()
    return data

def pprint(thing):
    #PP.PrettyPrinter(indent=4).pprint(thing)
    for x in thing:
        print(('{}'*len(x)).format(*x))

def get_board(x, y):
    board = [ [ '-' for _ in range(x)  ] for _ in range(y) ]
    # INIT STATE
    board[INIT_Y][INIT_X] = 'H'
    return board

def read_moves(data, board):

       # ROW, COL
    H = [INIT_Y, INIT_X]

    knots = [
        ["H", INIT_Y, INIT_X],
        ["1", INIT_Y, INIT_X],
        ["2", INIT_Y, INIT_X],
        ["3", INIT_Y, INIT_X],
        ["4", INIT_Y, INIT_X],
        ["5", INIT_Y, INIT_X],
        ["6", INIT_Y, INIT_X],
        ["7", INIT_Y, INIT_X],
        ["8", INIT_Y, INIT_X],
        ["9", INIT_Y, INIT_X],
    ]

    H = knots[0][1], knots[0][2]

    for i, (dir, amt) in enumerate(data):

        for _ in range(int(amt)):
            
            if board[knots[0][1]][knots[0][2]] == 'h':
                board[knots[0][1]][knots[0][2]] = '#'
            else:
                board[knots[0][1]][knots[0][2]] = '-'

            # Move Head
            match dir:
                case 'R':
                    knots[0][2] += 1
                case 'L':
                    knots[0][2] -= 1
                case 'U':
                    knots[0][1] -= 1
                case 'D':
                    knots[0][1] += 1
                case _:
                    pass

            if board[knots[0][1]][knots[0][2]] == '#':
                board[knots[0][1]][knots[0][2]] = '#'
            # else:
            #     board[knots[0][1]][knots[0][2]] = 'H'

            for i in range(0, len(knots)-1):
                h_key = knots[i][0]
                # board[knots[i][1]][knots[i][2]] = '-'

                t_key = knots[i+1][0]
                # board[knots[i+1][1]][knots[i+1][2]] = '-'

                tmp_a = knots[i+1][1]
                tmp_b = knots[i+1][2]

                if knots[i][1] == knots[i+1][1] and knots[i][2] == knots[i+1][2]:
                    break

                # Move Tail according to Head position
                # Scenario 1: Row or Col
                if knots[i][1] == knots[i+1][1]: # Same row
                    if knots[i][2] - knots[i+1][2] == 2: # Head Right 2
                        knots[i+1][2] += 1
                    elif knots[i+1][2] - knots[i][2] == 2: # Head Left 2
                        knots[i+1][2] -= 1
                elif knots[i][2] == knots[i+1][2]: # Same col
                    if knots[i+1][1] - knots[i][1] == 2: # Head Up 2
                        knots[i+1][1] -= 1
                    elif knots[i][1] - knots[i+1][1] == 2: # Head Down 2
                        knots[i+1][1] += 1
                # Scenario 2: Diagonal
                elif knots[i+1][2] - knots[i][2] == 1: # Head Left 1
                    if knots[i][1] - knots[i+1][1] == 2: # Head Down 2
                        knots[i+1][2] -= 1
                        knots[i+1][1] += 1
                    elif knots[i][1] - knots[i+1][1] == -2: # Head Up 2
                        knots[i+1][2] -= 1
                        knots[i+1][1] -= 1
                elif knots[i][2] - knots[i+1][2] == 1: # Head Right 1
                    if knots[i][1] - knots[i+1][1] == 2: # Head Down 2
                        knots[i+1][2] += 1
                        knots[i+1][1] += 1
                    elif knots[i][1] - knots[i+1][1] == -2: # Head Up 2
                        knots[i+1][2] += 1
                        knots[i+1][1] -= 1
                elif knots[i][1] - knots[i+1][1] == 1: # Head Down 1
                    if knots[i+1][2] - knots[i][2] == 2: # Head Left 2
                        knots[i+1][1] += 1
                        knots[i+1][2] -= 1
                    elif knots[i][2] - knots[i+1][2] == 2: # Head Right 2
                        knots[i+1][1] += 1
                        knots[i+1][2] += 1
                elif knots[i+1][1] - knots[i][1] == 1: # Head Up 1
                    if knots[i+1][2] - knots[i][2] == 2: # Head Left 2
                        knots[i+1][1] -= 1
                        knots[i+1][2] -= 1
                    elif knots[i][2] - knots[i+1][2] == 2: # Head Right 2
                        knots[i+1][1] -= 1
                        knots[i+1][2] += 1
                elif knots[i+1][1] - knots[i][1] == 2: # Head Up 2
                    if knots[i+1][2] - knots[i][2] == 2: # Head Left 2
                        knots[i+1][1] -= 1
                        knots[i+1][2] -= 1
                    elif knots[i][2] - knots[i+1][2] == 2: # Head Right 2
                        knots[i+1][1] -= 1
                        knots[i+1][2] += 1
                elif knots[i][1] - knots[i+1][1] == 2: # Head Down 2
                    if knots[i+1][2] - knots[i][2] == 2: # Head Left 2
                        knots[i+1][1] += 1
                        knots[i+1][2] -= 1
                    elif knots[i][2] - knots[i+1][2] == 2: # Head Right 2
                        knots[i+1][1] += 1
                        knots[i+1][2] += 1
                # if board[knots[i+1][1]][knots[i+1][2]] == board[knots[i][1]][knots[i][2]]:

                # if knots[i+1][1] == tmp_a and knots[i+1][2] == tmp_b:
                #     break

                # if knots[i][1] != knots[i+1][1] and knots[i][2] != knots[i+1][2]:
                if t_key == '9':
                    board[tmp_a][tmp_b] = '#'
                # else:
                #     board[tmp_a][tmp_b] = '-'

                # if board[knots[i+1][1]][knots[i+1][2]] != 'H':
                #     board[knots[i+1][1]][knots[i+1][2]] = t_key
                
                # print()
                # print("( " + dir + " , " + amt + " ) " + str(i) + '/' + str(len(data)))
                # pprint(board)

            # print()
            # print("( " + dir + " , " + amt + " ) " + str(i) + '/' + str(len(data)))
            # pprint(board)

    #         board[t[0]][t[1]] = '#'
    
    # if board[knots[0][1]][knots[0][2]] == 'h':
    #     board[knots[0][1]][knots[0][2]] = '#'
    # else:
    #     board[knots[0][1]][knots[0][2]] = '-'
    
    # board[t[0]][t[1]] = '#'

    # print('done')
    # pprint(board)

    return board

def main():
    #data = read_data("TestData.txt")
    #data = read_data("TestData2.txt")
    data = read_data("Data.txt")
    #pprint(data)
    #print()

    board = get_board(X, Y)
    #pprint(board)

    read_moves(data, board)
    #print()
    #pprint(board)
    
    flatten_list = list(chain.from_iterable(board))
    
    total = flatten_list.count('#') + flatten_list.count('h')
    
    print()
    print('total travelled spaces of tail:')
    print(total)

if __name__=='__main__':
    main()