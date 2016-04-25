'''
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
'''

class Solution:    #可以做到in-place.  #bottom-up更加简单
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]
#从倒数第二行开始， 往上走。

'''
class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        l = len(triangle)
        dp = [0]*l
        for row in triangle:
            dp1 = dp[:]
            for i in range(len(row)):
                if i==0:  dp[i] =dp1[i]+ row[i]
                elif i==len(row)-1: dp[i] = dp1[i-1]+row[i]
                else: dp[i] = min(dp1[i-1], dp1[i]) + row[i]
        return min(dp)

    #We use 2 arrays. dp for the current row, dp1 for the last row.    We scan each position in each row.    O(n2) time ,  O(n) space
    # naive solution,  DFS,  polynomial time and space. ..
    # #use recursion.
'''