'''
 Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

'''
class Solution: ##http://yucoding.blogspot.com/2013/08/leetcode-question-133-palindrome.html
# O(n2) space, O(n2) time
    # @param s, a string
    # @return an integer
    def minCut(self, s):   #双DP。 得到isPal是dp。  ret用ret[i-1]也是dp
        l = len(s);  ret = [i for i in range(l)]
        isPal = [[False]*l for i in range(l)]   #l+1也可以。 不用l+1也可以。 不用l+1, 有j - i <= 1足够
        for j in range(l):
            for i in range(j, -1, -1): # j+1主要是为了保证isPal的正确性
                 if s[i] == s[j] and (j - i <= 1 or isPal[i+1][j-1] == True):    # j是递增 ，已经保证了
                    isPal[i][j] = True
                    ret[j] =0 if i==0 else min(ret[i-1]+1, ret[j])        # when i ==0   .  the whole string [0:j] is a palindrom          #   i~j pal。 i-1
        return ret[l-1]
'''   O(n2) time and O(n) space.  So it is a better one
class Solution: ##http://yucoding.blogspot.com/2013/08/leetcode-question-133-palindrome.html
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        n = len(s)
        minCut = [i-1 for i in range(n+1)]
        for i in range(n):
            j = 0
            while i-j>=0 and i+j< n and s[i-j] == s[i+j]:
                minCut[i+j+1] = min(minCut[i+j+1], 1+ minCut[i-j])
                j+=1
            j = 1
            while i-j+1>=0 and i+j<n and s[i-j+1] == s[i+j]:
                minCut[i+j+1] = min(minCut[i+j+1], 1+ minCut[i-j+1])
                j+=1
        return minCut[n]  #https://oj.leetcode.com/discuss/9476/solution-does-not-need-table-palindrome-right-uses-only-space
'''