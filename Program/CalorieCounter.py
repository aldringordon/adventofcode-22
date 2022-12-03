class CalorieCounter():

    def __init__(self):
        self.total = []
        self.caloriesDict = {}
    
    def read_data(self, filename):
        self.total = []
        cals=[]
        f = open(filename, "r")
        for l in f:
            if l.strip():
                cals.append(int(l))
            else:
                self.total.append(cals)
                cals = []
        f.close()
        return
    
    def get_total(self):
        return self.total

    def count_calories(self):
        self.caloriesDict = dict([ (k+1, sum(v)) for k, v in enumerate(self.total) ])
    
    def read_and_convert(self, filename):
        print('Reading Calorie Data')
        self.read_data(filename)

        print('Calculating Calories')
        self.count_calories()

        print('Done')

    def get_max_key(self):
        return max(self.caloriesDict, key=self.caloriesDict.get)
    
    def get_max_val(self):
        return max(self.caloriesDict.values())
    
    def remove_max(self):
        del self.caloriesDict[self.get_max_key()]