'''
Description:

Count the number of prime numbers less than a non-negative number, n.
'''
class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n<2: return 0  #从i*i开始, 因为小于i的prime数之前已经考虑过了
        noprimes = set(j for i in range(2, int(n**0.5)+1) for j in range(i*i, n+1, i))  #来自sieve Prime.py
        return n-len(noprimes)-2   #除去1, n

'''
class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        isPrime = [True] * max(n, 2)
        isPrime[0], isPrime[1] = False, False
        x = 2
        while x * x < n:
            if isPrime[x]:
                p = x * x
                while p < n:
                    isPrime[p] = False
                    p += x
            x += 1
        return sum(isPrime)
'''