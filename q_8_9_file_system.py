import time
ISOTIMEFORMAT=’%Y-%m-%d %X’
#  date = time.strftime(ISOTIMEFORMAT, time.localtime())

class Entry:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.created = time.strftime(ISOTIMEFORMAT, time.localtime())
        self.lastUpdated = self.created
        self.lastAccessed = self.created
        
    def delete(self):
        if self.paret == None: return False
        return self.parent.deleteEntry(this)
        
    def getFullPath(self):
        if not self.parent: return self.name
        return self.parent.getFullPath() + '/' + self.name
        
class File(Entry):
    def __init__(self, name, parent, size， content = None):
        Entry.__init__(name, parent)
        self.size = size
        self.content = content
        
        
class Directory(Entry):
    def __init__(self, name, parent, contents = []):
        Entry.__init__(name, parent)
        self.contents = contents
        self.size = 0
        if len(self.contents) >0:
            for e in self.contents:
                self.size += e.size
    
    def addEntry(self, entry):
        self.contents.append(entry)
        
    def deleteEntry(self, entry):
        return self.contents.pop(entry)
        
    def numberOfFiles(self):
        count = 0
        for e in self.contents:
            if isInstance(e, File): count+=1
            elif isInstance(e, Directory):
                count += self.numberOfFiles(e)
        return count
        
        
    
        
    
    
        
    