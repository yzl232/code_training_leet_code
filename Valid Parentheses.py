'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''
#facebook考过。  先说...
class Solution:
    # @return a boolean
    def isValid(self, s):   #因为不用求最长的长度，所以只要存入种类就好了 。 求maxlength存入index。remove存入index
        l = {'(':0, '{':1, '[':2}
        r = {')':0, '}':1, ']':2}
        stack = []
        for ch in s:
            if ch in l: stack.append(l[ch])
            elif ch in r:
                if not stack or stack.pop()!=r[ch]: return False
        return not stack #空得话返回True