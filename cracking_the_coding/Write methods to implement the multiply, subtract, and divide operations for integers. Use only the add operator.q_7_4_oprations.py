class Operations:
    def __init__(self):
        pass

    def negate(self, a):
        neg = 0
        if a>0:
            while a>0:
                tmp = -1
                a+=tmp
                neg+=tmp
                while a+tmp>0:
                    a+=tmp
                    neg += tmp
                    tmp+=tmp
        elif a<0:
            while a<0:
                tmp = 1
                a+=tmp
                neg+=tmp
                while a+tmp<0:
                    a+=tmp
                    neg += tmp
                    tmp+=tmp
        return neg

    def minus(self, a, b):
        return a + self.negate(b)

    def abs(self, a):
        if a<0: return self.negate(a)
        return a

    def multiplication(self, a, b):
        if a<b: return self.multiplication(b, a)
        result = 0
        for i in range(0, self.abs(b)):
            result+=a
        if b<0:
            result = self.negate(result)
        return result

# leetcode
    def divide(self, dividend, divisor):  # obvious we can only use plus/minus operation
        sign = 1 if (dividend > 0 and divisor >0) or (dividend <0 and divisor <0) else -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0
        while dividend >= divisor:
            k = 1; tmp = divisor
            while dividend >= tmp:
                result += k
                dividend -= tmp
                tmp += tmp
                k+=k
        if sign == -1: return 0-result
        return result