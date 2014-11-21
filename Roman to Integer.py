'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''


class Solution:
    # @return an integer
    def romanToInt(self, s):
        transSingleTable = {"I":1, "V":5, "X":10, "L":50, "C":100, "M":1000, "D":500}
        transDoubleTable = {"IV":4, "IX":9, "XL": 40, "XC":90, "CD":400, "CM":900}
        result = 0
        index = 0

        roman = s.upper()
        while index < len(s):
            if index < len(s) -1 and roman[index: index+2] in transDoubleTable:
                result += transDoubleTable[roman[index: index+2]]
                index +=2
            elif roman[index] in transSingleTable:
                result += transSingleTable[roman[index]]
                index +=1
        return result