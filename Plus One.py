class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        carry = 0
        n = len(digits)
        for i in range(n-1, -1, -1):
            digits[i] =digits[i]  + 1 if i==n-1 else digits[i]+carry
            if digits[i] == 10:
                digits[i] = 0
                carry = 1
            else:     return digits
        return [1]+digits