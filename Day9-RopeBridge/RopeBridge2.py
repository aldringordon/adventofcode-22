import pprint as PP
from itertools import chain
from Knot import Knot

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

def print_board(thing):
    for i in range(len(thing), 0, -1):
        x = thing[i-1]
        print(('{}'*len(x)).format(*x))
    # for x in thing:
    #     print(('{}'*len(x)).format(*x))

def read_moves(data):
    
    head = Knot()
    k1 = Knot()
    k2 = Knot()
    k3 = Knot()
    k4 = Knot()
    k5 = Knot()
    k6 = Knot()
    k7 = Knot()
    k8 = Knot()
    k9 = Knot()

    BOARD = [ ['.' for _ in range(15)] for _ in range(15)]

    for ins, amt in data:
        for _ in range(int(amt)):
            
            # BOARD[int(head.y)][int(head.x)] = '.'
            # BOARD[int(tail.y)][int(tail.x)] = '.'

            head.move(ins, 1)
            k1.move_toward(head)
            k2.move_toward(k1)
            k3.move_toward(k2)
            k4.move_toward(k3)
            k5.move_toward(k4)
            k6.move_toward(k5)
            k7.move_toward(k6)
            k8.move_toward(k7)
            k9.move_toward(k8)

            # BOARD[int(head.y)][int(head.x)] = 'H'
            # BOARD[int(tail.y)][int(tail.x)] = 'T'
            # BOARD[int(tail.y)][int(tail.x)] = '#'

            # print()
            # print(ins, amt)
            # print("head: ", str(head.get_pos()))
            # print("tail: ",str(tail.get_pos()))
            # print_board(BOARD)
    
    print_board(BOARD)
    print(head.get_visited())
    print(k9.get_visited())
    print(len(k9.get_visited()))
    pass

def main():
    data = read_data("Data.txt")
    #data = read_data("Data.txt")
    #pprint(data)
    #print()

    read_moves(data)
    
    
    print()

if __name__=='__main__':
    main()