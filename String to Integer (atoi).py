'''
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.
'''
class Solution:
    # @return an integer
    def myAtoi(self, s):   # 不用考虑边界'#'       #s[i]=='',   i+=1 这样子用pointer也很好。
        sign = 1; ret=0; i=0; s=s.strip()+'#' 
        if s[i]=='+':    i+=1
        elif s[i]=='-':
            sign = -1
            i+=1
        while '0'<=s[i]<='9':
            ret =ret*10 + ord(s[i])-ord('0')
            i+=1
        return max(min(ret*sign, 2147483647 ), -2147483648)