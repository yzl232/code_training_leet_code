'''
 A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.

'''


class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        n = len(s)
        if n==0 or s[0] == '0' : return 0
        ppre = pre= cur = 1
        for i in range(2, n+1):
            cur = 0
            if s[i-1] != '0':  cur+=pre
            if '10' <= s[i-2:i] <= '26': cur+=ppre
            ppre, pre = pre, cur
        return cur

'''
class Solution:
    # @param s, a string
    # @return an integer

    def numDecodings(self, s):
        return self.dfs(s)

    def dfs(self, s):
        if len(s)==0:
            return 1
        t = 0
        if s[0]!='0':
            t+=self.dfs(s[1:])  #一个非0字符
        if len(s)>=2 and  '10'<=s[:2]<='26':
            t+=self.dfs(s[2:]) #2个字符
        return t

'''