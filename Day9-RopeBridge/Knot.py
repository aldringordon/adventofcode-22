
MOVE_TABLE = {
    '(2, -2)': 'UL',
    '(2, -1)': 'UL',
    '(1, -2)': 'UL',

    '(2, 0)': 'L',
    
    '(2, 1)': 'DL',
    '(2, 2)': 'DL',
    '(1, 2)': 'DL',

    '(0, 2)': 'D',

    '(-1, 2)': 'DR',
    '(-2, 2)': 'DR',
    '(-2, 1)': 'DR',

    '(-2, 0)': 'R',

    '(-2, -1)': 'UR',
    '(-2, -2)': 'UR',
    '(-1, -2)': 'UR',

    '(0, -2)': 'U',
}

class Knot():
    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.visited = []
        pass

    def move_up(self, amount):
        self.y += amount
    
    def move_down(self, amount):
        self.y -= amount
    
    def move_left(self, amount):
        self.x -= amount
    
    def move_right(self, amount):
        self.x += amount
    
    def move(self, direction, amount):
        match direction:
            case 'U':
                self.move_up(amount)
            case 'D':
                self.move_down(amount)
            case 'L':
                self.move_left(amount)
            case 'R':
                self.move_right(amount)

    def get_pos(self):
        return self.x, self.y

    def calc_difference(self, knot):
        x = self.x - knot.x
        y = self.y - knot.y
        return x, y
    
    def move_toward(self, knot):
        pos_diff = self.calc_difference(knot)
        if str(pos_diff) in MOVE_TABLE:
            move = MOVE_TABLE.get(str(pos_diff))
            for x in move:
                self.move(x, 1)
        self.check_visited()
    
    def check_visited(self):
        # Check visited tile before moving
        if not str(self.get_pos()) in self.visited:
            self.visited.append(str(self.get_pos()))

    def get_visited(self):
        return self.visited