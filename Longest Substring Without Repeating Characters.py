'''
Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
'''
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        maxLen=0;  d = {}; tail = 0
        for head in range(len(s)):
            ch = s[head]
            if ch in d:   tail=max(d[ch] + 1, tail)
            d[ch] = head
            maxLen = max(maxLen, head-tail+1)
        return maxLen