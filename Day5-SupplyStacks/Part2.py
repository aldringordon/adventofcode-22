import re

def read_data(filename):
    stackData = []
    instructions = []

    readStack = True

    f = open(filename, "r")
    for l in f:
        if l.strip():
            if readStack:
                stackData.append(re.findall('.{1,4}', l))
            else:
                instructions.append(l.strip())
        else:
            readStack = False

    f.close()
    
    stack = [[] for i in range(len(stackData[0]))]

    for row in stackData[0:-1]:
        for i, col in enumerate(row):
            if col.strip():
                stack[i].insert(0, col.strip(' []'))

    return stack, instructions

def printStack(stack):
    printstack = [ [ ' ' for i in range(len(stack))] for i in range(max([len(i) for i in stack]))]

    for i, col in enumerate(stack):
        for j, e in enumerate(col):
            printstack[j][i] = e
        
    for i in range(len(printstack)-1, -1, -1):
        print(printstack[i])

    for i in range(len(stack)):
        print('  ' + str(i) + '  ', end='')
    print('')

def main():

    #stack, instructions = read_data("TestData.txt")
    stack, instructions = read_data("Data.txt")
    
    printStack(stack)

    for x in instructions:
        insts = re.findall(r"\d+", x)
        move = int(insts[0])
        source = int(insts[1])
        dest = int(insts[2])
        
        if move == 1 and source == 8 and dest ==5:
            breakpoint

    #     print()
    #     print(x)
    #     print(move, source, dest)
    #     print('- before:')
    #     print(stack[source-1], str(len(stack[source-1])))
    #     print(stack[dest-1], str(len(stack[dest-1])))

        if move == 26:
            print('hi')

        tmp = []

        for i in range(move):
            # if len(stack[source-1]) > 0:
            #     stack[dest-1].append(stack[source-1].pop())
            tmp.append(stack[source-1].pop())
        
        while len(tmp) > 0:
            stack[dest-1].append(tmp.pop())

    #     print('- after:')
    #     print(stack[source-1], str(len(stack[source-1])))
    #     print(stack[dest-1], str(len(stack[dest-1])))
    
    print()
    ans = ''
    for i, col in enumerate(stack):
        print(i, col)
        if len(col) > 0:
            print(col[-1])
            ans += col[-1]
    
    print(ans)

if __name__=="__main__":
    main()