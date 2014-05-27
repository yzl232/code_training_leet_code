class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        n = len(points)
        if n<3: return n
        result = -1
        for i in range(n):
            slope = {'inf': 0}
            samePointNum = 1
            for j in range(n):
                if i == j : continue
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    samePointNum +=1
                elif points[i].x == points[j].x and points[i].y != points[j].y:
                    slope['inf']+=1
                elif points[i].x != points[j].x:
                    k = 1.0 *  ( points[i].y - points[j].y) / (points[i].x - points[j].x)
                    slope[k] = 1 if k not in slope else slope[k]+1
            result = max(result, max(slope.values()) + samePointNum)
        return  result