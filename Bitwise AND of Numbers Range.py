'''
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.

Credits:
Special thanks to @amrsaqr for adding this problem and creating all test cases.
'''
# http://www.shuatiblog.com/blog/2015/05/10/Bitwise-AND-of-Numbers-Range/
class Solution:
    # @param m, an integer
    # @param n, an integer
    # @return an integer
    def rangeBitwiseAnd(self, m, n):   #除了公共头部, 只要有一个0bit. AND一定是0.
        p = 0  #这样解释, 某个bit位出现三次以上, 就一定是0.   那么找只出现2次且一样的部分. 
        while m != n:
            m >>= 1
            n >>= 1
            p += 1
        return m << p