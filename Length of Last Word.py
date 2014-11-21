'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.
'''
class Solution:
    def lengthOfLastWord(self, s):
        if not s: return 0
        i = len(s)-1
        while i>=0 and s[i]==' ': i-=1
        i2 = i
        while i2>=0 and s[i2]!=' ': i2-=1
        return i-i2

'''
class Solution:
    def lengthOfLastWord(self, s):
        return len(s.strip().split(" ")[-1])
'''