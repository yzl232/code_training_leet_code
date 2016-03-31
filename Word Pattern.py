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
    def wordPattern(self, s, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        t = str.split()
        return [s.find(x) for x in s] == [t.index(x) for x in t]  # map(s.find, s) == map(t.index, t)
        
'''
s ="aabb"
>>> map(s.find, s)
[0, 0, 2, 2]

相同的字符串都是相同的数字。  
'''