MAX_SIZE = 5

        
class Hash:
    def __init__(self, items = [[] for i in range(MAX_SIZE)]):
        self.items = items
    
    def hashCodeOfKey(self, key):
        return len(str(key)) % len(self.items) 
    
    def put(self, key, val):
        x = self.hashCodeOfKey(key)
        if len(self.items[x]) == 0: 
            self.items[x].append((key, value))
        else:
            if (key, value) in self.items[x]:
                self.items[x].remove((key, value))
            self.items[x].append((key, value))
    
    def get(self, key):
        x = self.hashCodeOfKey(key)
        if len(self.items[x]) == 0: return 
        for c in self.items[x]:
            if c[0] == key:
                return c[1]
        return 
                
                
                 
        
        
    
    
        
    