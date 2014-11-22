'''
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.
'''
class Solution:
    # @return an integer
    def atoi(self, s):
        s = s.strip()
        if s =='':return 0
        new = ''
        temp = s
        if s[0] in ['+', '-']:
            new+=s[0]
            temp = s[1:]
        
        if temp == '':return 0
        if temp[0] >'9' or temp[0]<'0':return 0
        for ch in temp:
            if '0'<=ch<='9':new +=ch
            else: break
        if new == '':return 0
        result = int(new)
        if result>2147483647: return 2147483647
        if result < -2147483648:return -2147483648
        return result
                
        