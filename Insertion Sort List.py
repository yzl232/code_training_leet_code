'''
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
'''
class Solution:
    # @return a string
    def intToRoman(self, n):
        ret = ""
        vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        nums = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        for i in range(len(vals)):
            v = vals[i]
            cnt , n = n/v, n%v
            ret +=nums[i]*cnt
        return ret