'''
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
'''
# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, arr):
        n = len(arr); ret = 0
        if n<3: return n
        for i in range(n):
            d = {'inf': 0};  same = 1
            for j in range(n):
                if i == j : continue
                if arr[i].x == arr[j].x and arr[i].y == arr[j].y:    same +=1
                elif arr[i].x == arr[j].x and arr[i].y != arr[j].y:   d['inf']+=1
                else:
                    k = 1.0 *  ( arr[i].y - arr[j].y) / (arr[i].x - arr[j].x)
                    if k not in d: d[k]=0
                    d[k]+=1
            ret = max(ret, same+max(d.values()))
        return  ret