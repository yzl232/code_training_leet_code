'''
 Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
'''

class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        carry =0; ret=''
        i=len(a)-1;  j=len(b)-1
        while i>=0 or j>=0 or carry:
            s = carry+(0 if i<0 else int(a[i]))+(0 if j<0 else int(b[j]))
            carry, s = s/2, s%2
            ret = str(s)+ret
            i-=1; j-=1
        return ret



'''
class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        la, lb = len(a), len(b)
        l = max(la, lb)
        if la>lb:  return self.addBinary(b, a)
        a = '0'*(lb-la)+a
        carry =0; ret=''
        for i in range(len(a)-1, -1, -1):
            s = carry+ord(a[i])-ord('0')+ord(b[i])-ord('0')
            carry, s = s/2, s%2
            ret = str(s)+ret
        if carry==1: ret = '1'+ret
        return ret
'''