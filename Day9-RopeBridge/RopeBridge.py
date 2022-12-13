import pprint as PP
from itertools import chain

def read_data(filename):
    data = []
    f = open(filename, "r")
    for l in f:
        if l.strip():
            data.append(tuple(l.split()))
    f.close()
    return data

def pprint(thing):
    PP.PrettyPrinter(indent=4).pprint(thing)

def get_board(x, y):
    board = [ [ '-' for _ in range(x)  ] for _ in range(y) ]
    # INIT STATE
    board[Y//2][X//2] = 'H'
    return board

def read_moves(data, board):

       # ROW, COL
    h = [Y//2, X//2]
    t = [Y//2, X//2]

    for i, (dir, amt) in enumerate(data):

        for _ in range(int(amt)):
            
            if board[h[0]][h[1]] == 'h':
                board[h[0]][h[1]] = '#'
            else:
                board[h[0]][h[1]] = '-'
            
            board[t[0]][t[1]] = '#'

            # Move Head
            match dir:
                case 'R':
                    h[1] += 1
                case 'L':
                    h[1] -= 1
                case 'U':
                    h[0] -= 1
                case 'D':
                    h[0] += 1
                case _:
                    pass

            

            if board[h[0]][h[1]] == '#':
                board[h[0]][h[1]] = 'h'
            else:
                board[h[0]][h[1]] = 'H'
            # Move Tail according to Head position

            # Scenario 1: Row or Col

            if h[0] == t[0]: # Same row
                if h[1] - t[1] == 2: # Head Right 2
                    t[1] += 1
                elif t[1] - h[1] == 2: # Head Left 2
                    t[1] -= 1
            elif h[1] == t[1]: # Same col
                if t[0] - h[0] == 2: # Head Up 2
                    t[0] -= 1
                elif h[0] - t[0] == 2: # Head Down 2
                    t[0] += 1

            # Scenario 2: Diagonal
            elif t[1] - h[1] == 1: # Head Left 1
                if h[0] - t[0] == 2: # Head Down 2
                    t[1] -= 1
                    t[0] += 1
                elif h[0] - t[0] == -2: # Head Up 2
                    t[1] -= 1
                    t[0] -= 1
            
            elif h[1] - t[1] == 1: # Head Right 1
                if h[0] - t[0] == 2: # Head Down 2
                    t[1] += 1
                    t[0] += 1
                elif h[0] - t[0] == -2: # Head Up 2
                    t[1] += 1
                    t[0] -= 1
            
            elif h[0] - t[0] == 1: # Head Down 1
                if t[1] - h[1] == 2: # Head Left 2
                    t[0] += 1
                    t[1] -= 1
                elif h[1] - t[1] == 2: # Head Right 2
                    t[0] += 1
                    t[1] += 1
            
            elif t[0] - h[0] == 1: # Head Up 1
                if t[1] - h[1] == 2: # Head Left 2
                    t[0] -= 1
                    t[1] -= 1
                elif h[1] - t[1] == 2: # Head Right 2
                    t[0] -= 1
                    t[1] += 1
            
            board[t[0]][t[1]] = 'T'

            if board[h[0]][h[1]] == 'T':
                board[h[0]][h[1]] = 'H'

            #print()
            print("( " + dir + " , " + amt + " ) " + str(i) + '/' + str(len(data)))
            # pprint(board)
    
    if board[h[0]][h[1]] == 'h':
        board[h[0]][h[1]] = '#'
    else:
        board[h[0]][h[1]] = '-'
    
    board[t[0]][t[1]] = '#'

    # print('done')
    # pprint(board)

    return board

X = 500
Y = 500

def main():
    #data = read_data("TestData.txt")
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