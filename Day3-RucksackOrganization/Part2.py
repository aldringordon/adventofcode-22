def get_val(item):
    if('a' <= item <= 'z'):
        return ord(item) - 96
    else:
        return ord(item) - 38

def get_common(list_triple):
    return list(set(list_triple[0]).intersection(list_triple[1]).intersection(list_triple[2]))

def split_data(data):
    str1 = data[0:len(data)//2]
    str2 = data[len(data)//2:]
    return (str1, str2)

def read_data(filename):
    data = []
    group = []

    f = open(filename, "r")
    for l in f:
        group.append(list(l.strip()))
        if len(group) == 3:
            data.append(group)
            group = []
    f.close()
    return data

if __name__=="__main__":
    data = read_data("Data.txt")
    sum = 0
    for x in data:
        # common = get_common(split_data(x))
        common = get_common(x)
        for y in common:
            sum += get_val(y)
    print("sum: ")
    print(sum)