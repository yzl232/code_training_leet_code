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
#有点像regular match.
class Solution:
    def wordPatternMatch(self, p, s):  #p: pattern.
        self.d = {}
        return self.dfs(p, s)

    def dfs(self, p, s):
        if not p and not s:  return True  #举例就可以了..  剩下的要大于len(p)-(i+1)
        if not p or len(p)>len(s):   return False
        for i in range(len(s)): # +2 because it is the "end of an end"
            if p[:1] not in self.d and s[:i+1] not in self.d.values():   
                self.d[p[:1]] = s[:i+1]   # 1和i+1对应. 实际上就是p[0]
                if self.dfs(p[1:], s[i+1:]):  return True
                del self.d[p[:1]]
            elif p[:1] in self.d and self.d[p[0]] == s[:i+1] and self.dfs(p[1:], s[i+1:]):  return True
        return False
'''
class Solution:
    def wordPatternMatch(self, p, s):  #p: pattern.
        self.d, self.words = {}, set()
        return self.dfs(p, s)

    def dfs(self, p, s):
        if not p and not s:  return True  #举例就可以了..  剩下的要大于len(p)-(i+1)
        if (not p and s) or len(p)>len(s):   return False
        for i in range(len(s)): # +2 because it is the "end of an end"
            if p[0] not in self.d and s[:i+1] not in self.words:
                self.d[p[0]] = s[:i + 1];  self.words.add(s[:i + 1])
                if self.dfs(p[1:], s[i+1:]):  return True
                del self.d[p[0]];  self.words.remove(s[:i + 1])
            elif p[0] in self.d and self.d[p[0]] == s[:i+1] and self.dfs(p[1:], s[i+1:]):  return True
        return False
'''