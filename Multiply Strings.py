'''
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.
'''

class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, a, b):
        a, b = a[::-1], b[::-1]
        total = [0]*(len(a) + len(b))
        for i in range(len(a)):
            for j in range(len(b)):
                total[i + j] += int(a[i]) * int(b[j])
        carry, ret = 0, []
        for x in total:
            x+=carry
            carry, s = x/10, x%10
            ret.append(str(s))     #也append的反面  ret.insert(0, str(s % 10))
        while len(ret) >= 2 and ret[-1] == "0": ret.pop()
        return ''.join(ret[::-1])