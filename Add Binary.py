class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        la = len(a); lb = len(b)
        if la > lb:
            b = '0' * (la - lb) + b
            l = la
        else:
            a = '0'*(lb - la) + a
            l = lb
        a = a[::-1]; b = b[::-1]
        solution = ''
        carry = 0
        for i in range(l):
            tmp = ord(a[i]) - ord('0') + ord(b[i]) - ord('0')  + carry
            solution += str(tmp%2)
            carry = tmp/2
        if carry == 1:
            solution += '1'
        return  solution[::-1]
