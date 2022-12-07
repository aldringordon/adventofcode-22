from Directory import Directory

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

    fileSys.printContents()

    dirs = fileSys.getAllSubdirs()

    print()
    sizeSum = []
    sizeList = []
    for subDir in dirs:
        size = subDir.getSize()

        if size <= 100000:
            sizeList.append(subDir.name)
            sizeSum.append(size)

            print()
            print(subDir.name)
            print(size)
    
    print()
    print("totals:")
    print(sizeList)
    print(sizeSum)
    print(sum(sizeSum))

    # x = Directory("testDir")
    # x.addDirectory("test2DIR")
    # x.addFile("testFile", 100)
    # x.addFile("abcdef", 100)

    # z = x.getDirectory("test2DIR")
    # z.addFile("test2DIRFile", 200)
    # z.addFile("a2DIRFile", 200)
    # z.addFile("aawgeawegRFile", 200)

    # x.printContents()

    # print(z.getSize())
    # print(x.getSize())

if __name__=='__main__':
    main()