# encoding=utf-8
'''
Design an algorithm to find the kth number such that the only prime factors are 3,5, and 7
'''

#G家最近考过
class Solution(object):
    def nthUglyNumber(self, n):
        i2 = i3 = i5 = 0;  ret = [1]
        for i in range(n-1):
            m = min(ret[i2]*2, ret[i3]*3, ret[i5]*5)
            ret.append(m)
            if m == ret[i2]*2: i2+=1
            if m == ret[i3]*3: i3+=1
            if m == ret[i5]*5: i5+=1  
        return ret[-1]
# # 这样子理解, 因为ret已经排好序了, 是最小的了.    下一个ugly number肯定是最小的*2,  *3,  *5.
#print '%d th element, %d, c3:%d, c5:%d, c7: %d' % (i, ret[i], c3, c5, c7)

'''
这样子理解, 因为ret已经排好序了, 是最小的了.    下一个ugly number肯定是最小的*2,  *3,  *5.   

对于三个ordered list来说,  
 ret[0] * 2,  ret[1] * 2,  ret[2] * 2
 ret[0] * 3,  ret[1] * 3,  ret[2] * 3

Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence
1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, …
shows the first 11 ugly numbers. By convention, 1 is included.
Write a program to find and print the 150’th ugly number.



initialize
   ugly[] =  | 1 |
   i2 =  i3 = i5 = 0;

First iteration
   ugly[1] = Min(ugly[i2]*2, ugly[i3]*3, ugly[i5]*5)
            = Min(2, 3, 5)
            = 2
   ugly[] =  | 1 | 2 |
   i2 = 1,  i3 = i5 = 0  (i2 got incremented )

Second iteration
    ugly[2] = Min(ugly[i2]*2, ugly[i3]*3, ugly[i5]*5)
             = Min(4, 3, 5)
             = 3
    ugly[] =  | 1 | 2 | 3 |
    i2 = 1,  i3 =  1, i5 = 0  (i3 got incremented )

Third iteration
    ugly[3] = Min(ugly[i2]*2, ugly[i3]*3, ugly[i5]*5)
             = Min(4, 6, 5)
             = 4
    ugly[] =  | 1 | 2 | 3 |  4 |
    i2 = 2,  i3 =  1, i5 = 0  (i2 got incremented )

Fourth iteration
    ugly[4] = Min(ugly[i2]*2, ugly[i3]*3, ugly[i5]*5)
              = Min(6, 6, 5)
              = 5
    ugly[] =  | 1 | 2 | 3 |  4 | 5 |
    i2 = 2,  i3 =  1, i5 = 1  (i5 got incremented )

Fifth iteration
    ugly[4] = Min(ugly[i2]*2, ugly[i3]*3, ugly[i5]*5)
              = Min(6, 6, 10)
              = 6
    ugly[] =  | 1 | 2 | 3 |  4 | 5 | 6 |
    i2 = 3,  i3 =  2, i5 = 1  (i2 and i3 got incremented )

Will continue same way till I < 150

'''

#G家这么考的。
'''
Given an equation in the form 2^i * 3^j * 5^k * 7^l where i,j,k,l >=0 are integers.write a program to generate numbers from that equation in sorted order efficiently.

1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12
'''

class Solution2:
    def primeN(self, n):  #用了3个pointer来记录
        c2 = c3 = c5 = c7 = 0
        ret = [1]
        for i in range(1, n+1):
            m = min(ret[c2]*2, ret[c3]*3, ret[c5]*5, ret[c7]*7)
            ret.append(m)
            if m== ret[c2]*2: c2+=1
            if m == ret[c3]*3: c3+=1
            if m == ret[c5]*5: c5+=1
            if m== ret[c7]*7: c7+=1
        return ret
s = Solution2()
print s.primeN(10)