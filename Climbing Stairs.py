'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''


class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return a

#有个log的解法  Fibonacci

'''
logN 解法。  利用了leetcode的求power部分

使用了matrix得power.
m=
[1 1]
[1 0]

m*m=
[2 1]
[1 1]


m*m*m=
[3 2]
[2 1]


[Fn+1, Fn]
[Fn, Fn-1]



class Solution2:
    def fib(self, n):
        self.x =  [[1, 1], [1, 0]]
        if n==0: return 0
        result = self.pow(n)
        return result[1][0]

    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, n):
        if n == 0:return 1
        elif n==1: return self.x
        elif n>1:
            half = self.pow(n/2)
            square = self.multiply(self.x, self.x)
            if n%2 == 0 : return square
            else: return self.multiply(square, self.x)
        else:
            return 1.0/self.pow(-n)

    def multiply(self, f, m):
        x = f[0][0] * m[0][0] + f[0][1] * m[1][0]
        y = f[0][0] * m[0][1] + f[0][1] * m[1][1]
        z =  f[1][0]*m[0][0] + f[1][1]*m[1][0]
        w = f[1][0]*m[0][1] +f[1][1]*m[1][1]
        return [[x, y], [z, w]]
Time Complexity: O(Logn)
Extra Space: O(Logn) if we consider the function call stack size, otherwise O(1).

'''