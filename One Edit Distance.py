# encoding=utf-8
'''
Given two strings S and T, determine if they are both one edit distance apart.
'''
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