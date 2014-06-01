class Solution:  #http://www.cnblogs.com/lichen782/p/leetcode_Largest_Rectangle_in_Histogram.html
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        height = [[0 for i in range(n)] for j in range(m)]
        maxArea = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    height[i][j] = height[i-1][j]+1 if i>0 else 1
        for i in range(m):
            maxArea = max(maxArea, self.largestRectangleArea(height[i]))
        return maxArea
    
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
                temp = stack.pop()   # keep poping while top of the stack is greater or the stack is empty
                if len(stack) !=0:
                    ret = max(height[temp]*(i-1-stack[-1]), ret) # the rightmost one as the boundry:  i-1
                else:# with every poped one as the smallest one
                    ret = max(height[temp] * i, ret)
        return ret