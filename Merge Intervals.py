'''
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
'''


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
class Solution: #思路就是排序后，检查前一个有没有重叠。 有就合并
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, arr):
        if len(arr) == 0:   return arr
        arr.sort(key = lambda x: x.start)
        ret = [arr[0]]
        for i in range(1, len(arr)):
            cur, pre = arr[i], ret[-1]
            if cur.start <= pre.end:  pre.end = max(pre.end, cur.end)   #只要更新pre.end就好。都不用真的插入
            else:   ret.append(cur)
        return ret


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