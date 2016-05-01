'''
 Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.
'''
class Solution:
    def isUgly(self, num):
        if num<=0: return False  # num=0要特别考虑， 不然下面死循环。
        for p in 2, 3, 5:
            while num % p == 0:    num /= p
        return num == 1