'''
 Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

'''

class Solution: ##http://yucoding.blogspot.com/2013/08/leetcode-question-133-palindrome.html
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        l = len(s)
        isPal = [[False for j in range(l)] for i in range(l)]
        minCutNum = [i for i in range(l)]
        for j in range(l):
            for i in range(j+1): # j+1主要是为了保证isPal的正确性
                 if s[i] == s[j] and (j - i <= 1 or isPal[i+1][j-1] == True):  
                    isPal[i][j] = True
                    if i== 0:  # when i ==0   .  the whole string [0:j] is a palindrome 
                        minCutNum[j] = 0
                    else: # actually we get the minimum of all minPalNum[i-1] + 1
                        minCutNum[j] = min(minCutNum[i-1]+1, minCutNum[j])
        return minCutNum[l-1]      
        
        
