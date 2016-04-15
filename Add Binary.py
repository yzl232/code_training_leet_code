'''
 Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
'''
#还是老方法最朴素最好了。  最容易的方法. 最好的方法.
class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        la, lb = len(a), len(b)
        if la>lb:  return self.addBinary(b, a)
        a = '0'*(lb-la)+a
        carry =0; ret=''
        for i in range(len(a)-1, -1, -1):
            s = carry+int(a[i])+int(b[i])
            carry, s = s/2, s%2
            ret = str(s)+ret
        return ret if not carry else '1'+ret


'''
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


'''
class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        carry =0; ret=''
        m=len(a); n=len(b)  #对于python一个指针足够。
        for i in range(-1, -max(m, n)-1, -1):   # -1~-n之间属于valid。
            s = carry+(0 if i<-m else int(a[i]))+(0 if i<-n else int(b[i]))
            carry, s = s/2, s%2
            ret = str(s)+ret
        return ret if not carry else '1'+ret
'''