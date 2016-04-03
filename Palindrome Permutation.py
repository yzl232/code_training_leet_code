'''
Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.
'''

'''
解法思路
Just check that no more than one character appears an odd number of times. Because if there is one, then it must be in the middle of the palindrome. So we can't have two of them.
'''

class Solution:
    def canPermutePalindrome(self, s):
        return sum(v % 2 for v in collections.Counter(s).values()) <= 1
