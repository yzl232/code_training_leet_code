class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        maxLen = 0
        substr = ''
        tail = 0
        for head in range(len(s)):
            if s[head] not in substr:
                substr += s[head]
            else:
                maxLen = max(maxLen, len(substr))
                while s[tail] != s[head]: tail+=1
                tail +=1
                substr = s[tail:head+1]
        maxLen = max(maxLen, len(substr))
        return maxLen