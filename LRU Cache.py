'''
 Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
'''
class ListNode:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, node):
        if self.tail is None:     self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
        self.head = node

    def delete(self, node):
        if node.prev:     node.prev.next = node.next
        else:       self.head = node.next
        if node.next:         node.next.prev = node.prev
        else:        self.tail = node.prev

class LRUCache:
    def __init__(self, capacity):
        self.cache = LinkedList()
        self.d = {}
        self.capacity = capacity

    def _insert(self, key, val):
        node = ListNode(key, val)
        self.cache.insert(node)
        self.d[key] = node

    def get(self, key):
        if key in self.d:
            val = self.d[key].val
            self.cache.delete(self.d[key])
            self._insert(key, val)
            return val
        return -1

    def set(self, key, val):
        if key in self.d:    self.cache.delete(self.d[key])
        elif len(self.d) == self.capacity:
            del self.d[self.cache.tail.key] #注意这 里的先后顺序。。。先DEL然后再removelast#######################
            self.cache.delete(self.cache.tail)
        self._insert(key, val)