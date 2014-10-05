class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        l = len(triangle)
        dp = [0 for i in range(l)]
        for row in triangle:
            oldDp = dp[:]
            for i in range(len(row)):
                if i==0:
                    dp[i] = oldDp[i]+ row[i]
                elif i == len(row)-1:
                    dp[i] = oldDp[i-1] + row[i]
                else:
                    dp[i] = min(oldDp[i-1], oldDp[i]) + row[i]
        return min(dp)
    #We use 2 arrays. dp for the current row, oldDp for the last row.    We scan each position in each row. 
    
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