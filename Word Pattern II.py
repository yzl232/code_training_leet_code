'''
Problem Description:

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.

Examples:

        pattern = "abab", str = "redblueredblue" should return true.
        pattern = "aaaa", str = "asdasdasdasd" should return true.
        pattern = "aabb", str = "xyzabcxzyabc" should return false. 

Notes:
You may assume both pattern and str contains only lowercase letters.

'''
class Solution:
    def wordPatternMatch(self, p, s):  #p: pattern.
        self.d = {}
        return self.dfs(p, s)

    def dfs(self, p, s):
        if not p and s:   return False
        if not p and not s:  return True  #举例就可以了..  剩下的要大于len(p)-(i+1)
        if len(s)<len(p): return False
        for i in range(len(s)): # +2 because it is the "end of an end"
            if p[0] not in self.d and s[:i+1] not in self.d.values():
                self.d[p[0]] = s[:i+1]
                if self.dfs(p[1:], s[i+1:]):  return True
                del self.d[p[0]]
            elif p[0] in self.d and self.d[p[0]] == s[:i+1]:
                if self.dfs(p[1:], s[i+1:]):  return True
        return False


'''
"aa"

"xxxxxx"     
'''