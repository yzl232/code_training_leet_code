'''
 Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
'''

class ListNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.pre = None

class DoubleLinkedList:
    def __init__(self):
        self.top =self.tail = None

    def insert(self, node):
        if not self.tail:     self.tail = self.top = node
        else:
            self.top.pre, node.next = node, self.top   #相互之间，前后逻辑性极强。 可以推导
            self.top = node  

    def delete(self, node):
        if node.pre:     node.pre.next = node.next    #右边都是node.next。  假如x， x=
        else:       self.top = node.next  #比较容易记忆。
        if node.next:         node.next.pre = node.pre #右边都是node.pre
        else:        self.tail = node.pre

class LRUCache:
    def __init__(self, capacity):
        self.cache, self.d, self.capacity = DoubleLinkedList(), {}, capacity

    def _insert(self, key, val):
        self.d[key] = ListNode(key, val)
        self.cache.insert(self.d[key])

    def get(self, key):
        if key in self.d:
            self.cache.delete(self.d[key])
            self._insert(key, self.d[key].val)    #这里还是创建了新的node来插入. 因为之前删掉的, node.next, pre没有清掉.
            return self.d[key].val
        return -1

    def set(self, key, val):
        if key in self.d:    self.cache.delete(self.d[key])   # 这部分是类似get的. 先删除, 再插入.
        elif len(self.d) == self.capacity:
            del self.d[self.cache.tail.key] #注意这 里的先后顺序。。。先DEL然后再removelast#######################
            self.cache.delete(self.cache.tail)
        self._insert(key, val)