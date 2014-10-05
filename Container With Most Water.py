class Solution:
    # @return an integer
    def maxArea(self, height):  # two point scan
        l = 0 #，如果宽度减少，同时左右两侧的板得最小值都得比原来的还要大，才能容纳更多的水
        r = len(height) - 1
        result = -1
        while l <= r:
            result = max(result, min(height[r] , height[l])*(r-l) )
            if height[l] <= height[r]:
                l+=1
            else:
                r -= 1
        return result