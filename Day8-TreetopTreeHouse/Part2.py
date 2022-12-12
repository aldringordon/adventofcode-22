def checkCol(lookup_map, row, idx):
    for i in range(0, len(row)):
        val = row[i]
        left = row[:i]
        right = row[i+1:]
        
        l = 0
        r = 0

        if left:
            left.reverse()
            for x in left:
                l += 1
                if val <= x:
                    break

        if right:
            for x in right:
                r += 1
                if val <= x:
                    break

        if lookup_map[i][idx] == 0:
            lookup_map[i][idx] = l * r
        else:
            lookup_map[i][idx] *= l * r

def checkRow(lookup_map, row, idx):
    for i in range(0, len(row)):
        val = row[i]
        left = row[:i]
        right = row[i+1:]
        
        l = 0
        r = 0

        if left:
            left.reverse()
            for x in left:
                l += 1
                if val <= x:
                    break

        if right:
            for x in right:
                r += 1
                if val <= x:
                    break

        if idx == 3 and i ==2:
            pass
        lookup_map[idx][i] = l * r

# ['2', '5', '5', '1', '2']
# ['0', '5', '5', '3', '5']

def checkTrees(data):

    num_visible = 0

    lookup_map = [ [0 for _ in range(len(data[0]))] for _ in range(len(data)) ]

    for idx in range(1, len(data)-1):
        row = data[idx]
        col = [ x[idx] for x in data]
        checkRow(lookup_map, row, idx)
        checkCol(lookup_map, col, idx)
    
    for row in lookup_map:
        print(row)
    print()

    # 89739

    lol = [ max(x) for x in lookup_map ]
    # print(lol)
    print(max(lol))


def read_data(filename):
    data = []
    f = open(filename, "r")
    for l in f:
        data.append(list(l.strip()))
    f.close()
    return data

def main():
    #data = read_data("TestData.txt")
    data = read_data("Data.txt")
    checkTrees(data)

if __name__=='__main__':
    main()