# encoding=utf-8
'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
'''

class Solution:
    def convertToTitle(self, n):
        ret = ''
        while n:
            n-=1
            d, n = n%26,  n/26  #因为以1为base。  每次减去1
            ret = chr(ord('A')+d)+ret #从右往左.      因为我们总是先解决低位的。 所以最后取反
        return ret
#虽然说可以同时计算第一位和最后一位， 但是一旦除法，  %的会消失， 所以先算mod， 也就是最右边的。