'''
 Given a string, find the length of the longest substring T that contains at most k distinct characters.

For example, Given s = “eceba” and k = 2,

T is "ece" which its length is 3. 
'''
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        l=0;  d = {};   ret = 0
        for r in range(len(s)):
            if s[r] not in d :   d[s[r]] = 0
            d[s[r]]+=1
            while len(d)>k:  #缩减窗口。  2可以改成k。不断删除dict。直到
                d[s[l]]-=1
                if d[s[l]] ==0:     del d[s[l]]
                l +=1
            ret = max(r-l+1, ret)
        return ret