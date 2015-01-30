'''
 Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack..

'''

class MinStack:
    # @param x, an integer
    def __init__(self):
        self.stack1 = [];  self.stack2 = []

    # @return an integer
    def push(self, x):
        self.stack1.append(x)  #小于或者等于。才push stack2
        if not self.stack2 or x <= self.stack2[-1]:   self.stack2.append(x)

    # @return nothing
    def pop(self):
        if self.stack1.pop() == self.stack2[-1]:    self.stack2.pop()  #cur与最小值相等。 pop stack2

    # @return an integer
    def top(self):
        return self.stack1[-1]

    # @return an integer
    def getMin(self):
        return self.stack2[-1]