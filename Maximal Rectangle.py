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
        arr.append(0); ret = 0;  stack = []    #stack储存递增的
        for i in range(len(arr)):    #加了一个0，  arr[stack[-1]] < arr[i]不会满足
            while stack and arr[i] < arr[stack[-1]]:   # 于是到最后i。 不断pop
                h = arr[stack.pop()]
                w = i if not stack else i - stack[-1] -1     #空stack相当于 -1
                ret = max(ret, w*h)
            stack.append(i)
        return ret