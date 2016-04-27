'''
Description:

Count the number of prime numbers less than a non-negative number, n.
'''
'''
Description:

Count the number of prime numbers less than a non-negative number, n.
'''
class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):   #来自sieve Prime.py  #除去1.  注意  小于 n
        return 0 if n<2 else n-1-len(set(j for i in range(2, int(n**0.5)+1) for j in range(i*i, n, i)))
        # range(i*i,  )    使用i*i 是因为

'''
class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        isPrime = [True] * max(n, 2)
        isPrime[0] = isPrime[1] = False
        for i in range(2, int(n**0.5)+1):
            if isPrime[i]:
                for j in range(i*i, n, i):
                    isPrime[j] = False
        return sum(isPrime)
'''