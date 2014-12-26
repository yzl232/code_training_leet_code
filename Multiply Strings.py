'''
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.
'''

class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        num1, num2 = num1[::-1], num2[::-1]
        ret = [0 for i in range(len(num1) + len(num2))]
        for i in range(len(num1)):
            for j in range(len(num2)):
                ret[i + j] += int(num1[i]) * int(num2[j])
        carry, total = 0, []
        for digit in ret:
            s = carry + digit
            carry = s / 10
            total.append(str(s%10)) #也append的反面  total.insert(0, str(s % 10))
        while len(total) >= 2 and total[-1] == "0": total.pop()
        return ''.join(total[::-1])