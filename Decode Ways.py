class Solution:
    # @param s, a string
    # @return an integer
    #  a little complicated:
    #   One = ( s[i-1] == '0' )
    # TWO = ( s[i-2:i] >= '10' and s[i-2:i] <= '26' )
    # if ONE and TWO: dp[i-1] + dp[i-2]
    # elif ONE: dp[i-1]
    # elif TWO: dp[i-2]
    #  else:   0
    def numDecodings(self, s):
        n = len(s)
        if n==0 or s[0] == '0': return 0
        dp = [0 for i in range(n+1)]
        dp[0] = 1; dp[1] = 1
        for i in range(2, n+1):
            one = (s[i-1] != '0')
            two = ('10'<= s[i-2: i] <='26')
            if one and two: 
                dp[i] = dp[i-1] + dp[i-2]
            elif one:
                dp[i] = dp[i-1]
            elif two:
                dp[i] = dp[i-2]
            else:
                dp[i] = 0
        return dp[n]