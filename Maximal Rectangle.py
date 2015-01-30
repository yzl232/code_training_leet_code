#Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.
class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if not matrix:   return 0
        m = len(matrix); n = len(matrix[0])  #每层找到一个histagram
        dpH = [[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dpH[i][j] = 1 if i == 0 else dpH[i-1][j] + 1    # use dp
        return max(self.lageRec(x) for x in dpH)# O(n2)    space O(N2)

    def lageRec(self, arr):
        arr.append(0); ret = 0;  lefts = []    #stack储存递增的. 也就是必须是递增的左边界
        for r in range(len(arr)):    #加了一个0，  arr[stack[-1]] < arr[i]不会满足
            while lefts and arr[lefts[-1]]>arr[r]:   # 于是到最后i。 不断pop。    保证stack的递增。
                h = arr[lefts.pop()]       #stack的元素只要大于arr[i]. 就不断pop
                w = r if not lefts else r - (lefts[-1]+1)   #左边界加1.  想象方块的左边界。就容易了     #空stack相当于 -1
                ret = max(ret, w*h)       #
            lefts.append(r)   #保持stack递增   此时为空或者arr[i]大。 可以append
        return ret