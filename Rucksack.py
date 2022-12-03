def get_val(item):
    if('a' <= item <= 'z'):
        return ord(item) - 96
    else:
        return ord(item) - 38

def get_common(list_tuple):
    return list(set(list_tuple[0]).intersection(list_tuple[1]))

def split_data(data):
    str1 = data[0:len(data)//2]
    str2 = data[len(data)//2:]
    return (str1, str2)

def read_data(filename):
    data = []

    f = open(filename, "r")
    for l in f:
        data.append(list(l.strip()))

    f.close()
    return data

if __name__=="__main__":
    data = read_data("Data.txt")
    sum = 0
    for x in data:
        common = get_common(split_data(x))
        for y in common:
            print(get_val(y))
            sum += get_val(y)
    print()
    print(sum)