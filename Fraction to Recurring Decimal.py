# encoding=utf-8
'''
Fraction to Recurring Decimal

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

    Given numerator = 1, denominator = 2, return "0.5".
    Given numerator = 2, denominator = 1, return "2".
    Given numerator = 2, denominator = 3, return "0.(6)".

'''

class Solution:
    # @return a string
    def fractionToDecimal(self, a, b):   #不考虑负号只要9行
        real, rest = divmod(abs(a), abs(b))
        ret = '-'+str(real) if (a*b<0) else str(real)
        dec = ''; i=0; d = {}     #hash是无序的，所以加个有序的decimal
        while rest and rest not in d:      #先更新hashmap。再乘以10. hashmap存的是循环开始位置  
            d[rest] = i;  rest *= 10        #这一步是核心之一。
            digit, rest= divmod(rest, abs(b))
            dec+=str(digit);  i+=1
        return (ret+'.' + dec if dec else ret) if rest==0 else ret+ '.' +dec[: d[rest]]+ '('+dec[ d[rest] :]+')'

'''
#这道题目主要利用了整数mod的思想
#利用了hashmap保存mod的余数remainder
'''