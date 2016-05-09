'''
'''

import collections

class MovingAverage(object):

    def __init__(self, size):
        self.queue = collections.deque(maxlen=size)


    def next(self, val):
        self.queue.append(val)
        return float(sum(self.queue))/len(self.queue)