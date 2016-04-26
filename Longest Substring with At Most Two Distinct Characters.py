'''
 Given a string, find the length of the longest substring T that contains at most 2 distinct characters.

For example, Given s = “eceba”,

T is "ece" which its length is 3. 
'''

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLongestSubstringTwoDistinct(self, s):
        l=0;  d = {};   ret = 0
        for r in range(len(s)):
            if s[r] not in d :   d[s[r]] = 0
            d[s[r]]+=1
            while len(d)>2:  #缩减窗口。  2可以改成k。不断删除dict。直到
                d[s[l]]-=1
                if d[s[l]] ==0:     del d[s[l]]
                l +=1
            ret = max(r-l+1, ret)
        return ret