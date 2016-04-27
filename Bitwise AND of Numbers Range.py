'''
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.

Credits:
Special thanks to @amrsaqr for adding this problem and creating all test cases.
'''
class Solution:
    # @param m, an integer
    # @param n, an integer
    # @return an integer
    def rangeBitwiseAnd(self, m, n):   #除了公共头部, 只要有一个0bit. AND一定是0.
        p = 0    #  and是找相同的部分， 也就是不变的部分， 
        while m != n:
            m >>= 1
            n >>= 1
            p += 1
        return m << p
'''
 例如对于如下m和n： 
        1101 00111101 –>m 
        1101 11111111 –>n 
        可以去掉的就是n的分割部分的1。
        所以结果其实就是m和n公共头部*/

'''