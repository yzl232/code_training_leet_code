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
        total = math.factorial(n)
        k = k%total-1;  seq = ''
        digits = [str(i) for i in range(1, n+1)]
        for x in range(n, 0, -1):  #n>0
            total = total/x
            i, k = k/total, k%total
            seq += digits.pop(i)
        return seq