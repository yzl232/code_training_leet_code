'''
Given an array of strings, return all groups of strings that are anagrams.

Note: All inputs will be in lower-case.
'''

class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        d = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            d[sorted_word] = [word] if sorted_word not in d else d[sorted_word]+[word]
        result = []
        for i in d:
            if len(d[i])>=2:result+=d[i]
        return result