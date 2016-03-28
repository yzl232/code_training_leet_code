# encoding=utf-8

'''
 A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
Find all strobogrammatic numbers that are of length = n.
For example,
Given n = 2, return ["11","69","88","96"].
'''
#以前做过。文件名字叫旋转对称数
class Solution:
    def findStrobogrammatic(self, n):
        nums = list('018') if n%2 else ['']  #如果n为偶数,  [empty string]
        twos = [("0", "0"), ("1", "1"), ("6", "9"),("8", "8"), ("9", "6")]
        while n > 1:
            n -= 2
            nums = [a + num + b for a, b in twos for num in nums]
        return nums

s = Solution()
for i in range(3):
    print s.findStrobogrammatic(i+1)
