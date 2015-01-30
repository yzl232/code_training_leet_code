'''
 Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
'''


class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        s = s.lower(); i=0; j = len(s)-1
        while i<j:
            while i<j and not ('a'<=s[i]<='z' or '0'<=s[i]<='9'): i+=1
            while i<j and not ('a'<=s[j]<='z' or '0'<=s[j]<='9'): j-=1
            if s[i] != s[j]: return False
            i+=1;   j-=1
        return True

'''
上面这个是in-place
class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        s = s.lower(); s1 = ''
        for ch in s:
            if 'a'<=ch<='z' or '0'<=ch<='9':s1+=ch
        return s1 == s1[::-1]
'''