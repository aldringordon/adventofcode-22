
def read_data(filename):
    data = []
    f = open(filename, "r")
    for l in f:
        if l.strip():
            data.append(l.strip().split())
    f.close()
    return data

def exec_prog(data):
    cycles = []
    x = 1
    cycles.append(x)
    for ins in data:
        if ins[0] == 'noop':
            cycles.append(x)
        elif ins[0] == 'addx' and ins[1]:
            cycles.append(x)
            cycles.append(x)
            x += int(ins[1])
    cycles.append(x)
    return cycles

def main():
    #data = read_data("TestData.txt")
    #data = read_data("TestData2.txt")
    data = read_data("Data.txt")
    cycles = exec_prog(data)
    
    print(cycles[20])
    print(cycles[60])
    print(cycles[100])
    print(cycles[140])
    print(cycles[180])
    print(cycles[220])

    sum = 0
    sum += cycles[20] * 20
    sum += cycles[60] * 60
    sum += cycles[100] * 100
    sum += cycles[140] * 140
    sum += cycles[180] * 180
    sum += cycles[220] * 220
    print(sum)


if __name__=="__main__":
    main()