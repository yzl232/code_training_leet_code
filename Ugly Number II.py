'''
 Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number. 
'''
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        c2 = c3 = c5 = 0  #思想简单。 就是每次比较3， 5， 7的倍数哪个最小。  然后每次更新pointer
        ret = [1]
        for i in range(n-1):
            m = min(ret[c2]*2, ret[c3]*3, ret[c5]*5)
            ret.append(m)
            if m == ret[c2]*2: c2+=1
            if m == ret[c3]*3: c3+=1
            if m== ret[c5]*5: c5+=1    #print '%d th element, %d, c3:%d, c5:%d, c7: %d' % (i, ret[i], c3, c5, c7)
        return ret[-1]