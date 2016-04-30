# encoding=utf-8

'''
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.
'''
#以前做过。文件名字叫旋转对称数

class Solution(object):
    def isStrobogrammatic(self, s):
        d =set(['69', '96', '00', '11', '88']);  n=len(s)
        return all(s[i]+s[n-1-i] in d for i in range(n/2+1))
    
'''
class Solution(object):
    def isStrobogrammatic(self, s):
        d =set(['69', '96', '00', '11', '88'])
        i=0; j=len(s)-1
        while i<=j:
            if (s[i]+s[j]) not in d: return False
            i+=1; j-=1
        return True
'''