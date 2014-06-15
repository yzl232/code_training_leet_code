class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        s1 = ''
        for i in s:
            if 'A'<=i<='Z' or 'a'<=i<='z':
                s1+=i.lower()
            elif '0'<=i<='9':
                s1+=i.lower()
        return  s1 == s1[::-1]