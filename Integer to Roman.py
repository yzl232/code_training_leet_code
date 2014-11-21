'''
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
'''

class Solution:
    # @return a string
    def intToRoman(self, num):
        output = ""
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        for i in range(len(values)):
            v = values[i]
            counts = num / v
            num = num % v
            for j in range(counts):
                output += numerals[i]
        return output