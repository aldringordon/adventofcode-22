def checkCol(lookup_map, row, idx):
    for i in range(1, len(row)-1):
        val = row[i]
        left = row[:i]
        right = row[i+1:]
        if val > max(left) or val > max(right):
            lookup_map[i][idx] = True

def checkRow(lookup_map, row, idx):
    for i in range(1, len(row)-1):
        val = row[i]
        left = row[:i]
        right = row[i+1:]
        if val > max(left) or val > max(right):
            lookup_map[idx][i] = True

# ['2', '5', '5', '1', '2']
# ['0', '5', '5', '3', '5']

def checkTrees(data):

    num_visible = 0

    lookup_map = [ [False for _ in range(len(data[0]))] for _ in range(len(data)) ]
    lookup_map[0] = [True for _ in range(len(lookup_map[0]))]
    lookup_map[len(lookup_map)-1] = [True for _ in range(len(lookup_map[0]))]
    for x in lookup_map[1:len(lookup_map)-1]:
        x[0] = True
        x[len(x)-1] = True

    for idx in range(1, len(data)-1):
        row = data[idx]
        col = [ x[idx] for x in data]
        checkRow(lookup_map, row, idx)
        checkCol(lookup_map, col, idx)
    
    for row in lookup_map:
        num_visible += sum(row)

    print(num_visible)

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