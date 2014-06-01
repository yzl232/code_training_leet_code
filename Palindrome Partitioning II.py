class Solution: ##http://yucoding.blogspot.com/2013/08/leetcode-question-133-palindrome.html
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        l = len(s)
        isPal = [[False for j in range(l)] for i in range(l)]
        minCutNum = [i for i in range(l)]
        for j in range(l):
            for i in range(j, -1, -1): # j: 0=>n.  [j-1]     i:j=>-1. [i+1]   ..
                 if s[i] == s[j] and (j - i <= 1 or isPal[i+1][j-1] == True):  
                    isPal[i][j] = True                   
        for j in range(l):
            for i in range(j+1):
                if isPal[i][j]:
                    if i== 0:  # when i ==0   .  the whole string [0:j] is a palindrome 
                        minCutNum[j] = 0
                    else: # actually we get the minimum of all minPalNum[i-1] + 1
                        minCutNum[j] = min(minCutNum[i-1]+1, minCutNum[j])
        return minCutNum[l-1]