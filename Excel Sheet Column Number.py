# encoding=utf-8
'''
Excel Sheet Column Number

Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
'''
class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        cur = 0  #有点像subset那种iteration.  不断改变自身的recursion
        for ch in s:  #每增加一位。 可能性*6
            cur = cur*26 + ord(ch)-ord('A') + 1   # 以1为base， 每次加1
        return cur