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
class NestedIterator(object):
    def __init__(self, nestedList):
        ints = []
        def collect(nestedList):
            for x in nestedList[::-1]:
                if x.isInteger():
                    ints.append(x.getInteger())
                else:
                    collect(x.getList())
        collect(nestedList)
        self.next = ints.pop
        self.hasNext = lambda: bool(ints)


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())


'''

class DeepIterator: #代码不长。可以背下
    def __init__(self, l):
        self.stack = l[::-1]
        self.advance()

    def advance(self):
        if self.stack and isinstance(self.stack[-1], list):
            cur = self.stack.pop()
            self.stack +=cur[::-1]
            self.advance()

    def hasNext(self):
        return False if not self.stack else True

    def next(self):
        x = self.stack.pop()
        self.advance()
        return x
'''