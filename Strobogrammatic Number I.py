# encoding=utf-8

'''
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.
'''
#以前做过。文件名字叫旋转对称数

class Solution(object):
    def isStrobogrammatic(self, s):
        """
        :type num: str
        :rtype: bool
        """
        d =set(['69', '96', '00', '11', '88'])
        i=0; j=len(s)-1
        while i<=j:
            if (s[i]+s[j]) not in d: return False
            i+=1; j-=1
        return True
 
'''
class Solution:
    def palin(self, s):
        d ={'0':'0', '1':'1', '6':'9', '9':'6', '8':'8'}
        i=0; j=len(s)-1
        while i<=j:
            if s[i] not in d or s[j] not in d: return False
            if d[s[i]]!=s[j]: return False
            i+=1; j-=1
        return True

'''
