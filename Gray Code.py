'''

The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2

Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.
'''


class Solution:
    # @return a list of integers
    def grayCode(self, n):
        ret = [0]
        for i in range(n):
            gap = 2**i   #例子。  n=3, gap=4
            ret += [x + gap for x in ret[::-1]]
        return ret

s = Solution()
print s.grayCode(5)

'''
Comparing n = 2: [0,1,3,2] and n=3: [0,1,3,2,6,7,5,4], we found that the first four numbers in case n=3 are the same as the the numbers in case n=4.  Besides, [6,7,5,4] = [2+4,3+4,1+4,0+4].
'''


'''
from up to down, then left to right

0   1   11  110
        10  111
            101
            100

start:      [0]
i = 0:      [0, 1]
i = 1:      [0, 1, 3, 2]
i = 2:      [0, 1, 3, 2, 6, 7, 5, 4]
'''


'''
class Solution:
    # @return a list of integers
    def grayCode(self, n):
        return [(i>>1)^i for i in range(2**n)]
# 这种数学解就失去了interview的意思了。
'''