from Monkey2 import Monkey
from alive_progress import alive_bar

def read_data(filename):
    data = []

    id = 0
    items = None
    operation = None
    test_val = None
    true_monkey = None
    false_monkey = None

    f = open(filename, "r")
    for l in f:
        if l.strip():
            line = l.strip().split()
            match line[0]:
                case 'Starting':
                    items = [ int(x.replace(',',"")) for x in line[2:]  ]
                case 'Operation:':
                    operation = line[3:]
                case 'Test:':
                    test_val = int(line[-1])
                case 'If':
                    if line[1] == 'true:':
                        true_monkey = int(line[-1])
                    else:
                        false_monkey = int(line[-1])
                case _:
                    pass
        else:
            monkey = Monkey(id, items, operation, test_val, true_monkey, false_monkey)
            data.append(monkey)
            id += 1
            items = None
            operation = None
            test_val = None
            true_monkey = None
            false_monkey = None
    f.close()

    if items != None:
        monkey = Monkey(id, items, operation, test_val, true_monkey, false_monkey)
        data.append(monkey)

    return data

def inspect(monkeys, rounds):
    with alive_bar(rounds) as bar:
        for i in range(rounds):
            for monk in monkeys:
                while monk.has_items():
                    monk.inspect_next()
                    if monk.has_throwable():
                        other, item = monk.get_throwable()
                        monkeys[other].give_item(item)
            bar()
    
    for monk in monkeys:
        print(monk)

def main():
    monkeys = read_data("TestData.txt")
    #data = read_data("Data.txt")
    
    inspect(monkeys, 10000)

    inspects = [ x.inspects for x in monkeys ]

    a = max(inspects)
    inspects.remove(a)

    b = max(inspects)

    print('highest:')
    print(a)
    print(b)
    print()
    print('monkey business:')
    print(a*b)

if __name__=="__main__":
    main()