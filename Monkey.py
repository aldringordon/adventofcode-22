class Monkey():

    def __init__(self, id, items, operation, test_value, true_monkey, false_monkey):
        self.id = id
        self.items = items
        self.op_val = 0
        self.operation = self.get_operation(operation)
        self.test_value = test_value
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.throw_to = []
        self.inspects = 0

    def __str__(self):
        return 'Monkey [' + str(self.id) + '] inspects: ' + str(self.inspects) + ' - items: ' + str(self.items)
    
    def mul(self, val):
        return val * self.op_val

    def add(self, val):
        return val + self.op_val

    def squ(self, val):
        return val * val
    
    def dou(self, val):
        return val + val

    def get_operation(self, op):
        if op[2] == 'old':
            match op[1]:
                case '*':
                    return self.squ
                case '+':
                    return self.dou
        else:
            self.op_val = int(op[2])
            match op[1]:
                case '*':
                    return self.mul
                case '+':
                    return self.add
        return None

    def give_item(self, item):
        self.items.append(item)

    def has_items(self):
        return len(self.items) > 0

    def inspect_next(self):
        self.inspects += 1
        item = self.items.pop(0)

        print('monkey [' + str(self.id) + '] inspects item: ' + str(item))

        # inspect
        item = self.operation(item)
        print('\top: ' + str(item))

        # bored
        item = item//3
        print('\tbored: ' + str(item))

        monkey = self.test(item)

        if monkey - self.true_monkey == 0:
            print('\tis divisible: ' + str(self.true_monkey))
        else:
            print('\tnot divisible: ' + str(self.false_monkey))

        self.throw_to.append((monkey, item))
        print('\tthrown to: ' + str(self.throw_to))

    def has_throwable(self):
        return len(self.throw_to) > 0
    
    def get_throwable(self):
        return self.throw_to.pop(0)

    def test(self, item):
        val = item % self.test_value
        print('\t' + str(item) + ' div by ' + str(self.test_value) + ' = ' + str(val))
        if val == 0:
            return self.true_monkey
        return self.false_monkey