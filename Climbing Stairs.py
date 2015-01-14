'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        a,b,x,y = 1,1,1,0
        while n>0:
            if n&1: x, y = a*x + b*y, b*x + y*(a-b)
            a,b = a*a + b*b, 2*a*b - b*b
            n/=2
        return x

'''
class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return a
'''

#有个logN的解法  Fibonacci



'''
power()
[x, y]


[a, b]
[b, a-b]

平方。
[a*a+b*b, a*b+b(a-b)  ]
[  ]
'''