'''
 Given a list of unique words. Find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]

Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
'''

class Solution(object):
    def palindromePairs(self, words):
        d = {x:i for i, x in enumerate(words)}
        ret = set()
        for i, x in enumerate(words):
            for j in range(len(words[i])+1):
                t1, t2 = x[:j],  x[j:]
                if t1[::-1] in d and d[t1[::-1]]!=i and t2 == t2[::-1]:
                    ret.add((i,d[t1[::-1]])) # j=0, t1 为空, 不在d
                if t2[::-1] in d and d[t2[::-1]]!=i and t1 == t1[::-1]:
                    ret.add((d[t2[::-1]],i)) # j=0会重复一次。  j=n为空. 不在d
        return list(list(x) for x in ret)