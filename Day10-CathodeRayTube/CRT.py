class CRT():

    def __init__(self):
        self.sprite = 1
        self.cycle = 0
        self.CRT = []
        self.buffer = []
        self.last = None
        self.ins = None

    def check_pos(self):

        cycle = (self.cycle - 1) % 40
        sprite = self.sprite % 40

        if cycle == sprite:
            return True

        # Left
        if sprite <= 1:
            if cycle <= 2:
                return True

        # Right
        if sprite >= 38:
            if cycle >= 37:
                return True

        if abs(cycle - sprite) <= 1:
            return True

        return False

    def update_sprite(self, num):
        self.sprite += num

    def process(self, ins):
        self.last = self.ins
        self.ins=ins
        if ins[0] == 'noop':
            self.process_cycle()
        elif ins[0] == 'addx' and ins[1]:
            self.process_cycle()
            self.process_cycle()
            self.update_sprite(int(ins[1]))
    
    def process_cycle(self):
        self.cycle += 1
        self.draw()

    def draw(self):
        if self.check_pos():
            self.CRT.append('#')
            self.buffer.append('#')
        else:
            self.CRT.append('.')
            self.buffer.append('.')
        
        if len(self.buffer) > 10:
            self.buffer.pop(0)
        