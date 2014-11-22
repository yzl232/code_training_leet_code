'''
Implement int sqrt(int x).

Compute and return the square root of x.
'''

class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        left = 0
        right = x/2+1 # sqrt(C MAX_INT 2147483647)=46340.950001
        while left <= right:
            mid = (left + right) / 2
            if mid ** 2 <= x < (mid + 1) ** 2:
                return mid
            elif x < mid ** 2:
                right = mid - 1
            else:
                left = mid + 1