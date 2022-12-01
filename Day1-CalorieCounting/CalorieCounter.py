
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

def count_calories(inputList):
    caloriesDict = {}

    for i, val in enumerate(inputList):
        print(str(i) + ' ' + str(sum(val)))
        caloriesDict.update({ i+1: sum(val) })

    return caloriesDict

if __name__=="__main__":
    caloriesDict = count_calories(TEST_INPUT)
    