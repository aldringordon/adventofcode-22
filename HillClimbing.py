'''
S -> a
E -> z

a = lowest
z = highest

Move up, down, left, right
'''

from Map import Map

def read_data(filename):
    data = []
    f = open(filename, "r")
    for l in f:
        if l.strip():
            data.append(list(l.strip()))
    f.close()
    return data

def main():
    data = read_data("TestData.txt")
    
    map = Map(data)
    
    map.print_map()

if __name__=='__main__':
    main()