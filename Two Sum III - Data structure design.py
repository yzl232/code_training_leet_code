# encoding=utf-8
'''
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

For example,

add(1); add(3); add(5);
find(4) -> true
find(7) -> false

'''

class TwoSum:

    # initialize your data structure here
    def __init__(self):
        self.d = {}    #two sum需要存index。  这里返回True. False即可，存个数。 1个和2个是区别

    # @return nothing
    def add(self, x):
        if x not in self.d: self.d[x]=0
        self.d[x]+=1

    # @param value, an integer
    # @return a Boolean
    def find(self, val):
        for x in self.d:
            y = val-x
            if (x==y and self.d[x]>=2) or (x!=y and y in self.d): return True
        return False