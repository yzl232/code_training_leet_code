# encoding=utf-8
'''
Given two strings S and T, determine if they are both one edit distance apart.
'''
class Solution: #
    # @param s, a string
    # @param t, a string
    # @return a boolean
    def isOneEditDistance(self, s, t):  #
        m=len(s); n=len(t)
        for i in range(min(m, n)):
                if s[i] != t[i]: return  s[i+1 if m>=n else i :]== t[i+1  if n>=m else i :]  #
        return abs(m-n) == 1
'''
#aa,  aab
#aba  aaa
#aa,   baa
    观察几个例子， 遇到不等的时候， 除非是比较小的string。 长度相等或者更长的那个， 都是要i+1        
'''


'''
class Solution: #
    # @param s, a string
    # @param t, a string
    # @return a boolean
    def isOneEditDistance(self, s, t):  #
        m = len(s)
        n = len(t)
        if m<n: return self.isOneEditDistance(t, s)
        for i in range(n):
            if s[i]!=t[i]:
                return s[i+1:] == t[ (i+1 if m==n else i):]    #只有更短的string才不用跳过到i+1.
        return (m-n)==1
 
'''


'''
#aa,  aab
#aba  aaa
#aa,   baa
#总共就差1和长度相等2种情况。  长度相等很好解决。  差一也好解决。
#差1得两种情况:在末尾。 在前面或者中间。
class Solution:
    # @param s, a string
    # @param t, a string
    # @return a boolean
    def isOneEditDistance(self, s, t):  #背下就好, 才9行代码。 背下。
        m=len(s); n=len(t)  #保持n比较大
        if m>n: return self.isOneEditDistance(t, s)
        if n-m>1: return False
        i=0; shift = n-m
        while i<m and s[i]==t[i]: i+=1
        if i==m: return shift==1     #aaa,   aaab这种情况
        if shift==0: i+=1    #替换,跳过
        while i<m and s[i]==t[i+shift]: i+=1
        return i==m
'''