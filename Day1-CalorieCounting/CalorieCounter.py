
TEST_INPUT = [
    [1000, 2000, 3000,],
    [4000],
    [5000, 6000],
    [7000, 8000, 9000],
    [10000]
    ]

TEST_ANSWER = 4
TEST_ANSWER_INDEX = TEST_ANSWER - 1
TEST_ANSWER_AMOUNT = 24000

DATA_FILE = "Data.txt"

def read_data(filename):
    total = []
    cals = []

    f = open(filename, "r")
    for l in f:
        if l.strip():
            cals.append(int(l))
        else:
            total.append(cals)
            cals = []

    f.close()
    return total

def count_calories(inputList):
    caloriesDict = {}

    for i, val in enumerate(inputList):
        caloriesDict.update({ i+1: sum(val) })

    return caloriesDict

if __name__=="__main__":
    inputData = read_data(DATA_FILE)

    caloriesDict = count_calories(inputData)

    val1 = max(caloriesDict.values())
    maxKey = max(caloriesDict, key=caloriesDict.get)
    print(maxKey)
    print(caloriesDict[maxKey])
    print

    del caloriesDict[maxKey]

    val2 = max(caloriesDict.values())
    maxKey = max(caloriesDict, key=caloriesDict.get)
    print(maxKey)
    print(caloriesDict[maxKey])
    print

    del caloriesDict[maxKey]

    val3 = max(caloriesDict.values())
    maxKey = max(caloriesDict, key=caloriesDict.get)
    print(maxKey)
    print(caloriesDict[maxKey])
    print

    print('total:')
    print(val1+val2+val3)