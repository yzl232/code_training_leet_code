'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''

class Solution:
    # @return an integer
    def romanToInt(self, s):
        one = {"I":1, "V":5, "X":10, "L":50, "C":100, "M":1000, "D":500}
        two = {"IV":4, "IX":9, "XL": 40, "XC":90, "CD":400, "CM":900}
        i = 0
        ret = 0
        while i<len(s):
            if i<len(s)-1 and s[i:i+2] in two:
                ret+=two[s[i:i+2]]
                i+=2
            elif s[i] in one:
                ret+=one[s[i]]
                i+=1
        return ret