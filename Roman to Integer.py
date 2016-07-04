'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999..
'''

class Solution:
# @param {string} s
# @return {integer}
    def romanToInt(self, s):
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        return sum((-1 if roman[s[i]] < roman[s[i+1]] else 1) * roman[s[i]] for i in range(0, len(s) - 1))+roman[s[-1]]
# the last letter is always added. Except the last one, if one letter is less than its latter one, this letter is subtracted.
'''
    def romanToInt(self, s):
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        z = 0
        for i in range(0, len(s) - 1):
            z += roman[s[i]] * (-1 if roman[s[i]] < roman[s[i+1]] else 1)
        return z + roman[s[-1]]


    def romanToInt(self, s):
        one = {"I":1, "V":5, "X":10, "L":50, "C":100, "M":1000, "D":500}    # 1,  5蛮容易记忆
        two = {"IV":4, "IX":9, "XL": 40, "XC":90, "CD":400, "CM":900}   #  9,  4  容易记忆.
        i = 0;  ret = 0
        while i<len(s):
            if i<len(s)-1 and s[i:i+2] in two:
                ret+=two[s[i:i+2]]
                i+=2
            elif s[i] in one:
                ret+=one[s[i]]
                i+=1
        return ret
'''