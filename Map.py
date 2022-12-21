class Map():

    def __init__(self, map):
        self.map = map
        self.current = (0, 0)
        self.target = (0, 0)

        self.setup()
    
    def setup(self):
        for i, row in enumerate(self.map):
            for j, x in enumerate(row):
                match x:
                    case 'S':
                        self.map[i][j] = 'a'
                        self.current = (i, j)
                    case 'E':
                        self.map[i][j] = 'z'
                        self.target = (i, j)
                    case _:
                        pass

    def print_map(self, flipped=False):
        if flipped:
            for i in range(len(self.map), 0, -1):
                x = self.map[i-1]
                print(('{}'*len(x)).format(*x))
        else:
            for x in self.map:
                print(('{}'*len(x)).format(*x))
