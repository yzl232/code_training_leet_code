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
    def maxPoints(self, points):
        n = len(points); ret = -1
        if n<3: return n
        for i in range(n):
            slope = {'inf': 0};  same = 1
            for j in range(n):
                if i == j : continue
                if points[i].x == points[j].x and points[i].y == points[j].y:    same +=1
                elif points[i].x == points[j].x and points[i].y != points[j].y:   slope['inf']+=1
                else:
                    k = 1.0 *  ( points[i].y - points[j].y) / (points[i].x - points[j].x)
                    if k not in slope: slope[k]=0
                    slope[k]+=1
            ret = max(ret, max(slope.values()) + same)
        return  ret