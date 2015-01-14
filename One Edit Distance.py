# encoding=utf-8
'''
Given two strings S and T, determine if they are both one edit distance apart.
'''

class Solution: #关键就是背下后面4行
    # @param s, a string
    # @param t, a string
    # @return a boolean
    def isOneEditDistance(self, s, t):  #背下就好
        for i in range(min(len(s), len(t))):
                if s[i] != t[i]: return  s[i+1 if len(s)>=len(t) else i :]== t[i+1 if len(t)>=len(s) else i :]
        return abs(len(s) - len(t)) == 1


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