# encoding=utf-8

'''
 Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

For example,

123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Hint:

    Did you see a pattern in dividing the number into chunk of words? For example, 123 and 123000.
'''
class Solution:
    def numberToWords(self, num):
        to19 = {0:"", 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
        tens = {20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'}
        def toWords(n):
            if n<20: return [to19[n]]
            if n<100: return [tens[n-n%10]] + toWords(n%10)    #0的部分.    默认为"".   结果为""变成zero.
            if n < 1000:    return [to19[n/100]] + ['Hundred'] + toWords(n%100)
            for i, w in enumerate(('Thousand', 'Million', 'Billion'), 1):  # 1000**1, 1000**2, 1000**3
                if n < 1000**(i+1):    return toWords(n/(1000**i)) + [w] + toWords(n%1000**i)
        return ' '.join(toWords(num)) or 'Zero'

s = Solution()
print s.numberToWords(20)
print s.numberToWords(1234520)