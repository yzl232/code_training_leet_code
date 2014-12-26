#Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.
class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if not matrix:   return 0
        m = len(matrix); n = len(matrix[0])
        height = [[0 for i in range(n)] for j in range(m)]
        ret = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    height[i][j] = 1 if i == 0 else height[i-1][j] + 1    # use dp
        for i in range(m):
            ret =max(ret, self.largestRectangleArea(height[i]))
        return  ret   # O(n2)    space O(N2)

    def largestRectangleArea(self, arr):
        stack = []
        i = 0; m = 0
        arr.append(0)
        while i < len(arr):
            if len(stack) == 0 or arr[i] >= arr[stack[-1]]:
                stack.append(i)
                i+=1
            else:
                t = stack.pop()
                m = max(m, arr[t] * i) if not stack else max(m, arr[t] * (i - 1 - stack[-1]))
        return  m