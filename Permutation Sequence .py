'''
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

    "123"
    "132"
    "213"
    "231"
    "312"
    "321"

Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
'''
class Solution:
    # @return a string
    def getPermutation(self, n, k):
        total = self.factorial(n)
        digits = [chr(ord('0') + i) for i in range(1, n+1)]
        seq = ''
        k -= 1
        while n>0:
            total = total/n
            i, k = divmod(k, total)
            seq += digits[i]
            digits.pop(i)
            n-=1
        return seq
            
        
    def factorial(self, n):
        result = 1
        for i in range(1, n+1):
            result *= i
        return result