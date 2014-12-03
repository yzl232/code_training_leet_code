# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        if len(intervals) == 0:
            return intervals
        intervals.sort(key = lambda x: x.start)
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            current, prev = intervals[i], result[-1]
            if current.start <= prev.end:
                prev.end = max(prev.end, current.end)
            else:
                result.append(current)
        return result


# NlogN 效率比以前高多了
'''
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
'''