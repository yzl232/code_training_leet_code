'''
Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

Example 2:
Given the list [1,[4,[6]]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6]. 
'''

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
#这道题目它自己的接口挺奇怪的。
class NestedIterator(object):
    def __init__(self, arr):
        self.st = arr[::-1]
        self.advance()

    def next(self):
        x = self.st.pop().getInteger()
        self.advance()
        return x

    def hasNext(self):
        return self.st != []

    def advance(self):
        while self.st and not self.st[-1].isInteger():  self.st = self.st[:-1] + self.st[-1].getList()[::-1]

'''
class NestedIterator: #代码不长。可以背下
    def __init__(self, l):
        self.st = l[::-1]
        self.advance()

    def advance(self):
        while self.st and isinstance(self.st[-1], list):  self.st = self.st[:-1] + self.st[-1][::-1]

    def hasNext(self):
        return self.st != []

    def next(self):
        x = self.st.pop()
        self.advance()
        return x
'''