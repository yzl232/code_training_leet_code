#Divide two integers without using multiplication, division and mod operator.
class Solution:
    # @return an integer
    def divide(self, dividend, divisor):  # obvious we can only use plus/minus operation 
        sign = 1 if (dividend > 0 and divisor >0) or (dividend <0 and divisor <0) else -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        while dividend >= divisor:
            k = 1; tmp = divisor
            while dividend >= tmp:
                quotient += k
                dividend -= tmp
                tmp += tmp
                k+=k
        if sign == -1: return 0-quotient
        return quotient
