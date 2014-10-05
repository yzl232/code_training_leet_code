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