class Solution:
    # @return a boolean
    def isPalindrome(self, x):  # just reverse integer 
        if x<0:return False
        y = x; rev = 0
        while y:
            rev, y = rev*10+y%10, y/10
        return x==rev

'''
class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x<0:return False
        div = 1
        while x / div >= 10 : div*=10
        while x >0:
            if x/div != x % 10:return False
            x, div = (x%div)/10, div/100
        return True


It turns out that comparing from the two ends is easier. First, compare the first and last digit. If they are not the same, it must not be a palindrome. If they are the same, chop off one digit from both ends and continue until you have no digits left, which you conclude that it must be a palindrome.
'''