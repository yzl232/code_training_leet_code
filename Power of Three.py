'''
 Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion? 
'''
'''
0  False
1 True
2 False
3  True
9   True
'''

class Solution(object):
    def isPowerOfThree(self, n):
        if n==0: return False
        while n%3==0: n/=3
        return n==1
# return n > 0 and 3 ** round(math.log(n,3)) == n
'''
class Solution(object):
    def isPowerOfThree(self, n):
        return n==1 or (n!=0 and n%3==0 and self.isPowerOfThree(n/3))

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n == 0 or n % 3 > 0:
            return False
        return self.isPowerOfThree(n / 3)



def isPowerOfThree(self, n):
    return n > 0 == 3**19 % n
'''