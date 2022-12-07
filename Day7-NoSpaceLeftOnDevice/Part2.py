from Directory import Directory

DISK_SPACE = 70000000
SPACE_NEEDED = 30000000

def read_data(filename):
    data = []

    f = open(filename)
    for l in f:
        data.append(l.strip())
    f.close()

    return data

def process_input(data):
    root = Directory("/", None)
    current = root
    for line in data:

        x = line.split()

        if x[0] == "$":
            if x[1] == "cd":
                if x[2] == "..":
                    current = current.getParent()
                elif x[2] == "/":
                    current = root
                else:
                    current = current.changeDirectory(x[2])
        else:
            if x[0] == 'dir':
                current.addDirectory(x[1])
            else:
                current.addFile(x[1], int(x[0]))
    
    return root

def main():
    #data = read_data("TestData.txt")
    data = read_data("Data.txt")

    fileSys = process_input(data)

    total = fileSys.getSize()
    available = DISK_SPACE - total
    needed = SPACE_NEEDED - available

    tmp = {}

    tmp2 = []
    for dir in fileSys.getAllSubdirs():
        if dir.getSize() >= needed:
            tmp.update({dir.getName(): dir.getSize()})
            tmp2.append(dir.getSize())
    
    print(tmp)
    print()
    print(min(tmp.values()))
    print(min(tmp, key=tmp.get))

    print()
    fuck = sorted(tmp2, key=int)
    print(fuck)
    print()

    print()
    print(fileSys.getName())
    print('total:\t\t', str(total))
    print('available:\t', str(available))
    print('needed:\t\t', str(needed))




if __name__=='__main__':
    main()