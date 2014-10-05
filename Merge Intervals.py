# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        result = []
        for i in intervals:
            result = self.insert(result, i)
        return  result


    def insert(self, intervals, newInterval):
        new = []
        temp = newInterval    # temp means to be deal with
        for i in intervals:
            if (temp.start > i.end):
                new.append(i)
            elif (temp.end < i.start):
                new.append(temp)
                temp = i
            else:
                temp = Interval(min(temp.start, i.start) , max(temp.end, i.end))
        new.append(temp)
        return new