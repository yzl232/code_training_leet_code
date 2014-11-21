'''
 Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
'''
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
        
