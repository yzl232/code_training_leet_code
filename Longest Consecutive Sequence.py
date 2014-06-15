class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        dict = {x:False for x in num} # False means not visited
        maxLen = -1
        for i in dict:
            if dict[i] == False:
                curr = i + 1; len1 = 0
                while curr in dict and dict[curr] == False:
                    len1 += 1; dict[curr] = True; curr += 1
                curr = i - 1; len2 = 0
                while curr in dict and dict[curr] == False:
                    len2 += 1; dict[curr] = True; curr -= 1
                maxLen = max(maxLen, 1 + len1 + len2)
        return maxLen