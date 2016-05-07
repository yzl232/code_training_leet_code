'''
 Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion? 
'''
class Solution(object):
    def isPowerOfFour(self, x):
            return x >= 1 and (x & (x - 1) == 0) and (x & 0xaaaaaaaa) == 0
'''
class Solution(object):
    def isPowerOfFour(self, num):
            return num >=1 and (num &(num-1) == 0) and (num & 0x55555555)== num
 #  4,  16,  64.
  #  2次方，  4次方，    6次方。。。 8次方。
#对应1, 3, 5, 7, 9...
判断一个数 x 是不是 2 的次幂只需要查看等式 ((x - 1) & x) == 0 是否成立。为什么？用 16 和 20 这两个数说明下就可以了。

16     : 00000000000000000000000000010000
16 - 1 : 00000000000000000000000000001111  这两个数相与结果为 0 。

20     : 00000000000000000000000000010100
20 - 1 : 00000000000000000000000000010011  这两个数相与结果不为 0 。

这样就很形象的说明了为什么这个表达式可以判断出一个数是不是 2 的次幂。

如果一个数是 2 的次幂，那么我们就可以接着判断这个数是不是 4 的次幂，因为 4 的次幂 1 所出现的位数一定是在奇数位，因此我们只需要用 01010101010101010101010101010101 （0x55555555）与上这个数，不为 0 就表示这个数是 4 的幂了，代码如下

public class Solution {
public boolean isPowerOfFour(int num) {
    if(num <= 0)
        return false;
    return ((num - 1) & num) == 0 && (num & 0x55555555) != 0; // 注意 & 的优先级比 == 低
}

}
'''