class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        s = s.lower(); s1 = ''
        for ch in s:
            if 'a'<=ch<='z' or '0'<=ch<='9':s1+=ch
        return s1 == s1[::-1]
        
        '''
         Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

        For example,
        "A man, a plan, a canal: Panama" is a palindrome.
        "race a car" is not a palindrome.

        Note:
        Have you consider that the string might be empty? This is a good question to ask during an interview.

        For the purpose of this problem, we define empty string as valid palindrome.
        '''