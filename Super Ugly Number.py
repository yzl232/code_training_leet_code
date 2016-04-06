# encoding=utf-8
'''
 Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

Note:
(1) 1 is a super ugly number for any given primes.
(2) The given numbers in primes are in ascending order.
(3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000. 
'''
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):  #用到三个array.   idx,  primes.  ret.
        d = {x:0 for x in primes}
        ret = [float('inf')]*n;  ret[0] = 1
        for i in xrange(1, n):
            ret[i] = min(ret[idx] * x for x, idx in d.items())
            for x, idx in d.items():
                if ret[i] == ret[idx]*x:  d[x]+=1
        return ret[-1]

s = Solution()
print s.nthSuperUglyNumber(9, [3, 5, 7])

#对比一下这个
'''
这样子理解, 因为ret已经排好序了, 是最小的了.    下一个ugly number肯定是最小的*2,  *3,  *5.   

对于三个ordered list来说,  
 ret[0] * 2,  ret[1] * 2,  ret[2] * 2
 ret[0] * 3,  ret[1] * 3,  ret[2] * 3




class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        c2 = c3 = c5 = 0
        ret = [1]
        for i in range(n-1):
            m = min(ret[c2]*2, ret[c3]*3, ret[c5]*5)
            ret.append(m)
            if m == ret[c2]*2: c2+=1
            if m == ret[c3]*3: c3+=1
            if m== ret[c5]*5: c5+=1    #print '%d th element, %d, c3:%d, c5:%d, c7: %d' % (i, ret[i], c3, c5, c7)
        return ret[-1]
'''
