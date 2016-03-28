# encoding=utf-8

'''
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to count the total strobogrammatic numbers that exist in the range of low <= num <= high.

For example,
Given low = "50", high = "100", return 3. Because 69, 88, and 96 are three strobogrammatic numbers.

Note:
Because the range might be a large number, the low and high numbers are represented as string.
'''
#以前做过。文件名字叫旋转对称数
class Solution:
    def findStrobogrammatic(self, n):
        nums = list('018') if n%2 else ['']  #如果n为偶数,  [empty string]
        while n>1:  #非得用while.  用for循环搞不定.
            n-=2   #大概是剩下的位数.     n<2, 只剩下一次扩充机会, 不能加上'00'
            nums = [a + x + b for a, b in '00 11 88 69 96'.split()[n<2:] for x in nums]   # [n<2:].  去除"00"
        return nums     #剩下的大于2位的时候, 才考虑增加00. a = b = "0" . 因为初位, 末尾不能加00. 所以剩下要大于2位.
# 连续的for是正常的先后顺序.  先循环a,b 后x
s = Solution()
for i in range(5):
    print s.findStrobogrammatic(i+1)
