#Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area. 
class Solution:
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
                    height[i][j] = 1 if i == 0 else height[i-1][j] + 1    # use dp
        for i in range(m):
            maxArea =max(maxArea, self.largestRectangleArea(height[i]))
        return  maxArea
            
                    
        
    def largestRectangleArea(self, height):
        stack = []
        i = 0; m = 0
        height.append(0)
        while i < len(height):
            if len(stack) == 0 or height[i] >= height[stack[-1]]:
                stack.append(i)
                i+=1
            else:
                temp = stack.pop()# keep poping while top of the stack is greater or the stack is empty
                m = max(m, height[temp] * i) if len(stack) == 0 else max(m, height[temp] * (i - 1 - stack[-1]))  # the rightmost one as the boundry:  i-1
        return  m      # with every poped one as the smallest one