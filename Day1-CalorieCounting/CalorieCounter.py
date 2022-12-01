import unittest

class TestCalorieCounter(unittest.TestCase):

    def setUp(self):
        self.inputData = read_data("TestData.txt")
        self.caloriesDict = count_calories(self.inputData)

    def test_answer(self):
        test_answer = 4
        key = max(self.caloriesDict, key=self.caloriesDict.get)
        self.assertEqual(test_answer, key, "answer did not match")

    def test_amount(self):
        test_amount = 24000
        value = max(self.caloriesDict.values())
        self.assertEqual(test_amount, value, "total amount did not match")

#end class

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
    return dict([ (k+1, sum(v)) for k, v in enumerate(inputList) ])

def main():

    # read data
    filename = "Data.txt"
    inputData = read_data(filename)

    # convert
    caloriesDict = count_calories(inputData)

    val1 = max(caloriesDict.values())
    maxKey = max(caloriesDict, key=caloriesDict.get)
    print("key=", str(maxKey))
    print("val=", str(caloriesDict[maxKey]))
    print()

    del caloriesDict[maxKey]

    val2 = max(caloriesDict.values())
    maxKey = max(caloriesDict, key=caloriesDict.get)
    print("key=", str(maxKey))
    print("val=", str(caloriesDict[maxKey]))
    print()

    del caloriesDict[maxKey]

    val3 = max(caloriesDict.values())
    maxKey = max(caloriesDict, key=caloriesDict.get)
    print("key=", str(maxKey))
    print("val=", str(caloriesDict[maxKey]))
    print()

    print('Total=')
    print(val1+val2+val3)

if __name__=="__main__":

    # tests
    #unittest.main()

    # main hacky shit
    main()