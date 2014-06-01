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