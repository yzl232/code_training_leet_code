'''
Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
'''
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        ret = 0; d={}; l = 0
        for r in range(len(s)):
            if s[r] in d: l=max(l, d[s[r]]+1)
            d[s[r]] = r
            ret = max(ret, r-l+1)
        return ret
# 考虑到asicii 256。 可以认为是O(256) space