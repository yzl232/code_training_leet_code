'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.
'''

class Solution:  #，如果宽度减少，同时左右两侧的板得最小值都得比原来的还要大，才能容纳更多的水
    # @return an integer
    def maxArea(self, height):  # two point scan
        l = 0; r = len(height)-1; result = 0
        while l<r:
            result = max(result, min(height[r], height[l])*(r-l))
            if height[r]>height[l]: l+=1
            else: r-=1
        return result