'''
 Implement the following operations of a queue using stacks.

    push(x) -- Push element x to the back of queue.
    pop() -- Removes the element from in front of queue.
    peek() -- Get the front element.
    empty() -- Return whether the queue is empty.

Notes:

    You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
    Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
    You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

'''
class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack1.append(x)

    # @return nothing
    def pop(self):
        self.peek()
        self.stack2.pop()

    # @return an integer
    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    # @return an boolean
    def empty(self):
        return len(self.stack1) + len(self.stack2) == 0
'''
enQueue(q,  x)
  1) Push x to stack1 (assuming size of stacks is unlimited).

deQueue(q)
  1) If both stacks are empty then error.
  2) If stack2 is empty
       While stack1 is not empty, push everything from satck1 to stack2.
  3) Pop the element from stack2 and return it.

'''