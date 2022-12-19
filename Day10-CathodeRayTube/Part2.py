from CRT import CRT

def read_data(filename):
    data = []
    f = open(filename, "r")
    for l in f:
        if l.strip():
            data.append(l.strip().split())
    f.close()
    return data

def pixel_position(current, x):
    return abs(current - x) == 1 or current == x

def exec_prog(data):
    crt = CRT()

    for ins in data:
        crt.process(ins)

    return crt

def print_board(thing):
    # for i in range(len(thing), 0, -1):
    #     x = thing[i-1]
    #     print(('{}'*len(x)).format(*x))
    for x in thing:
        print(('{}'*len(x)).format(*x))

LIT = '#'
DARK = '.'
BOARD = [ [DARK for _ in range(40)] for _ in range(6)]

def chunks(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]

def main():
    #data = read_data("TestData.txt")
    #data = read_data("TestData2.txt")
    data = read_data("Data.txt")
    crt = exec_prog(data)

    print(crt.CRT)

    chunk = chunks(crt.CRT, 40)
    print_board(chunk)
    
    # print(cycles[20])
    # print(cycles[60])
    # print(cycles[100])
    # print(cycles[140])
    # print(cycles[180])
    # print(cycles[220])

#     sum = 0
#     sum += cycles[20] * 20
#     sum += cycles[60] * 60
#     sum += cycles[100] * 100
#     sum += cycles[140] * 140
#     sum += cycles[180] * 180
#     sum += cycles[220] * 220
#     print(sum)
# # ...............###......................
#     print()
#     print_board(BOARD)

if __name__=="__main__":
    main()