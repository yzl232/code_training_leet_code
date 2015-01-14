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
        ret = '-' if  a*b<0 else ''
        a=abs(a); b=abs(b)
        real, rem = a / b,  a % b
        ret +=str(real)
        dec = ''; i=0; d = {}  #hash是无序的，所以加个有序的decimal
        while rem and rem not in d:
            d[rem] = i  #先更新hashmap。再乘以10. hashmap存的是循环开始位置
            rem *= 10  #这一步是核心之一。
            x, rem=rem/b, rem%b
            dec+=str(x); i+=1
        if rem==0:    return ret+'.' + dec if dec else ret
        i = d[rem]
        return ret+ '.' +dec[:i]+ '('+dec[i:]+')'