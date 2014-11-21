#Determine whether an integer is a palindrome. Do this without extra space.

class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x<0:return False
        k = 1
        while x / k >= 10 : k*=10
        while x >0:
            firstDigit = x/k
            if firstDigit != x % 10:return False
            x = (x- firstDigit * k)/10
            k /= 100
        return True

'''
It turns out that comparing from the two ends is easier. First, compare the first and last digit. If they are not the same, it must not be a palindrome. If they are the same, chop off one digit from both ends and continue until you have no digits left, which you conclude that it must be a palindrome.
'''