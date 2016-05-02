'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:

    pattern = "abba", str = "dog cat cat dog" should return true.
    pattern = "abba", str = "dog cat cat fish" should return false.
    pattern = "aaaa", str = "dog cat cat dog" should return false.
    pattern = "abba", str = "dog dog dog dog" should return false.

Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space. 

'''

class Solution(object):
    def wordPattern(self, p, s):
        """
        :type pattern: s1
        :type string: s
        :rtype: bool
        """
        t = s.split()
        d1, d2 = {x:i for i, x in enumerate(p)}, {x:i for i, x in enumerate(t)}
        return [d1[x] for x in p] == [d2[x] for x in t]
        #return [s1.find(x) for x in s1] == [t.index(x) for x in t]  # map(s.find, s) == map(t.index, t)
#和这道题一样的。 就是同样的x， 有相同index
# https://leetcode.com/problems/word-pattern/
        
'''
s ="aabb"
>>> map(s.find, s)
[0, 0, 2, 2]

相同的字符串都是相同的数字。  
'''