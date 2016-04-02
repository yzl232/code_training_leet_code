# encoding=utf-8

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        idx = [0]*len(primes)
        ugly = [float('inf')]*n;  ugly[0] = 1
        for i in xrange(1, n):
            ugly[i] = min(ugly[idx[j]] * primes[j] for j in xrange(len(primes)))
            for j in xrange(len(primes)):
                if ugly[i] == ugly[idx[j]]*primes[j]: idx[j] += 1
        return ugly[-1]

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
