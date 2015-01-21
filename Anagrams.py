'''
Given an array of strings, return all groups of strings that are anagrams.

Note: All inputs will be in lower-case.
'''
class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, arr):
        d = {}
        for w in arr:
            sortW = ''.join(sorted(w))
            if sortW not in d:  d[sortW]=[]
            d[sortW].append(w)
        ret = []
        for i in d:
            if len(d[i])>=2:ret+=d[i]
        return ret

#如果每个s很长，用array[26]或者hash 更佳。  如果chr的种类很多，比如asicii 256种，用sort比较好。