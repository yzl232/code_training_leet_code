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
        ret = [0]*(len(a) + len(b))
        for i in range(len(a)):
            for j in range(len(b)):
                ret[i + j] += int(a[i]) * int(b[j])
        carry, total = 0, []
        for x in ret:
            x+=carry
            carry, s = x/10, x%10
            total.append(str(s))     #也append的反面  total.insert(0, str(s % 10))
        return ''.join(total[::-1]).lstrip("0") or "0"
'''
class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, a, b):
        a, b = a[::-1], b[::-1]
        ret = [0]*(len(a) + len(b))
        for i in range(len(a)):
            for j in range(len(b)):
                ret[i + j] += int(a[i]) * int(b[j])
        carry, total = 0, []
        for x in ret:
            x+=carry
            carry, s = x/10, x%10
            total.append(str(s))     #也append的反面  total.insert(0, str(s % 10))
        while len(total) >= 2 and total[-1] == "0": total.pop()
        return ''.join(total[::-1])
'''