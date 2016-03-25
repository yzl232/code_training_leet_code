'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
'''
class Solution:   #特别需要例子, 不然看着都糊涂.
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        if len(s) != len(t): return False
        sourceMap, targetMap = {}, {}
        for i in range(len(s)):
            source, target = sourceMap.get(t[i]), targetMap.get(s[i])
            if not source and not target:
                sourceMap[t[i]], targetMap[s[i]] = s[i], t[i]
            elif target != t[i] or source != s[i]:
                return False
        return True