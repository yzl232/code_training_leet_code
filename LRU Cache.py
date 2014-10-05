class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.numItems = 0
        self.capacity = capacity
        self.d = collections.OrderedDict() 

    # @return an integer
    def get(self, key):
        try:
            temp = self.d[key]
            del self.d[key]
            self.d[key] = temp
            return temp
        except:
            return -1
            

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        try:
            del self.d[key]
            self.d[key] = value
            
        except:
            if self.numItems == self.capacity:
                self.d.popitem(last = False)
                self.d[key] = value
            else:
                self.d[key] = value
                self.numItems +=1
            
            ''''
             Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

            get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
            set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
            ''''