
def check_pairs(dataList):
    pairs = 0
    for a, b in dataList:

        if (a == '58-91'):
            print('hi')

        aLow, aHi = list(map(int, a.split('-')))
        bLow, bHi = list(map(int, b.split('-')))

        pair = False

        # A contains B
        if (aLow <= bLow and aHi >= bHi):
            pair = True
        elif (aLow >= bLow and aHi <= bHi):
            pair = True
        
        if pair:
            print(a, b)
            pairs += 1
    return pairs


def read_data(filename):
    data = []

    f = open(filename, "r")
    for l in f:
        pair = tuple(l.strip().split(','))
        data.append(pair)

    f.close()
    return data

def main():
    #data = read_data("TestData.txt")
    
    data = read_data("Data.txt")

    print(check_pairs(data))

if __name__=="__main__":
    main()