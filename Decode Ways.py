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
        if not s or s[0] == '0' : return 0
        ppre = pre= 1
        for i in range(1, len(s)):
            ppre, pre = pre, (pre if s[i]!="0" else 0) + (ppre if '10' <= s[i-1]+s[i] <= '26' else 0)
        return pre

'''
class Solution:
    # @param s, a string
    # @return an integer

    def numDecodings(self, s):
        if not s or s[0]=='0': return 0
        self.d={"":1}
        return self.dfs(s)

    def dfs(self, s):
        if s not in self.d:
            self.d[s] = (0 if s[0]=="0" else self.dfs(s[1:])) + (0 if not (len(s)>=2 and  '10'<=s[:2]<='26') else self.dfs(s[2:])) 
        return self.d[s]

class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        n = len(s)
        if n==0 or s[0] == '0' : return 0
        dp = [0 for i in range(n+1)]
        dp[0] = 1; dp[1] = 1
        for i in range(2, n+1):
            if s[i-1] != '0':  dp[i]+=dp[i-1]
            if '10' <= s[i-2:i] <= '26': dp[i]+=dp[i-2]
        return dp[-1]
'''