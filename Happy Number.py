'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

    1**2 + 9**2 = 82
    8**2 + 2**2 = 68
    6**2 + 8**2 = 100
    1**2 + 0**2 + 0**2 = 1

'''

class Solution(object):
    def isHappy(self, n):
        def getS(y):   return sum(int(x) ** 2 for x in str(y))
        slow, fast = getS(n), getS(getS(n))
        while slow != fast:   slow, fast = getS(slow), getS(getS(fast))
        return slow==1
#描述与 add digits类似， 但是这个是平方了， 那个没有平方。
'''
class Solution: # add digits
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        d = set()
        while n not in d:  
            d.add(n)
            n = sum(int(x) ** 2 for x in str(n))
        return n==1
'''