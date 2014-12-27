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
        d = {x:False for x in num} # False means not visited
        ret = 0
        for i in d:
            if not d[i]:
                a = i + 1;  b = i - 1
                while a in d and not d[a]:
                    d[a] = True; a += 1
                while b in d and not d[b]:
                    d[b] = True; b -= 1
                ret = max(ret, a-b-1)
        return ret


'''
class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        d = {x:False for x in num} # False means not visited
        maxLen = -1
        for i in d:
            if d[i] == False:
                cur = i + 1; len1 = 0
                while cur in d and d[cur] == False:
                    len1 += 1; d[cur] = True; cur += 1
                cur = i - 1; len2 = 0
                while cur in d and d[cur] == False:
                    len2 += 1; d[cur] = True; cur -= 1
                maxLen = max(maxLen, 1 + len1 + len2)
        return maxLen
'''