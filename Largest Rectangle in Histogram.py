'''
 Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given height = [2,1,5,6,2,3],
return 10. 
'''

class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        stack = []
        height.append(0)
        i = 0
        ret = 0
        while i<len(height):
            if len(stack)==0 or  height[stack[-1]] < height[i]:
                stack.append(i)
                i+=1
            else:
                temp = stack.pop()
                if len(stack) !=0:
                    ret = max(height[temp]*(i-1-stack[-1]), ret)
                else:
                    ret = max(height[temp] * i, ret)
        return ret