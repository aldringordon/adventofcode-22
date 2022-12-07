class Directory:

    class File:
        def __init__(self, name, size):
            self.name = name
            self.size = size
        
        def toString(self):
            return self.name + " (file, size=" + str(self.size) + ")"
        
        def getSize(self):
            return self.size

    def __init__(self, name, parent):
        self.name = name # String
        self.parent = parent # Directory
        self.dirs = []   # Directory
        self.files = []  # File
    
    def addFile(self, name, size):
        self.files.append( self.File(name, size) )

    def addDirectory(self, name):
        self.dirs.append( Directory(name, self) )
    
    def changeDirectory(self, name):
        for d in self.dirs:
            if name == d.name:
                return d
        return None
    
    def getParent(self):
        return self.parent

    def getSize(self):
        totalSize = 0
        for f in self.files:
            totalSize += f.getSize()
        for d in self.dirs:
            totalSize += d.getSize()
        return totalSize
    
    def getAllSubdirs(self):
        subDirs = []
        if self.name == "/":
            subDirs.append(self)
        for d in self.dirs:
            subDirs.append(d)
            subDirs += d.getAllSubdirs()
        return subDirs
    
    def getPath(self):
        if self.parent == None:
            return '.'
        else:
            return self.parent.getPath() + '/' + self.name

    def getName(self):
        return self.name

    def toString(self):
        return self.name + " (dir)"
    
    def printContents(self, indent="    "):
        print(indent + "> " + self.toString())
        if len(self.files) > 0:
            for file in self.files:
                print(indent + "    " + "- "+ file.toString())
        if len(self.dirs) > 0:
            for dir in self.dirs:
                dir.printContents(indent + "    ")
    
    def printDirectories(self, indent="    "):
        print(indent + "> " + self.toString())
        if len(self.dirs) > 0:
            for dir in self.dirs:
                dir.printDirectories(indent + "    ")