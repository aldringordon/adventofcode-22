from Djikstra import Graph

COST = 1

class Map():

    def __init__(self, map):
        self.map = map
        self.current = (0, 0)
        self.target = (0, 0)
        self.setup()
        self.g = Graph()
    
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

    def can_move(self, source, dest):
        if ord(source) - ord(dest) == -1:
            return True
        return False

    def get_moves(self, i, j):
        x = self.map[i][j]

        # Up
        if i > 0:
            if self.can_move(x, self.map[i-1][j]):
                self.g.add_edge(x, self.map[i-1][j], COST)

        # Down
        if i < len(self.map) - 1:
            if self.can_move(x, self.map[i+1][j]):
                self.g.add_edge(x, self.map[i+1][j], COST)

        # Left
        if j > 0:
            if self.can_move(x, self.map[i][j-1]):
                self.g.add_edge(x, self.map[i][j-1], COST)

        # Right
        if j < len(self.map[0]) - 1:
            if self.can_move(x, self.map[i][j+1]):
                self.g.add_edge(x, self.map[i][j+1], COST)

    def get_graph(self):
        return self.g

    def create_graph(self):
        
        # Create Vertices
        for row in self.map:
            for v in row:
                self.g.add_vertex(v)

        # Create Edges
        for i, row in enumerate(self.map):
            for j in range(len(row)):
                self.get_moves(i, j)