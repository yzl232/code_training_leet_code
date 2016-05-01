# encoding=utf-8

'''
 A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
Find all strobogrammatic numbers that are of length = n.
For example,
Given n = 2, return ["11","69","88","96"].
'''

class Solution:
    def findStrobogrammatic(self, n):
        nums = list('018') if n%2 else ['']  #如果n为偶数,  [empty string]
        for i in xrange(n/2):    #  i  次数. 每次+2.  有n/2次. 最后一次不能是00.  
            nums = [a + x + b for a, b in '00 11 88 69 96'.split()[i==n/2-1:] for x in nums]    
        return nums     #剩下的大于2位的时候, 才考虑增加00. a = b = "0" . 因为初位, 末尾不能加00. 所以剩下要大于2位.
#以前做过。文件名字叫旋转对称数

'''

>>> a, b = "00"
>>> a
'0'
>>> b
'0'


s= Solution()
for i in range(1, 10):
    print s.findStrobogrammatic(i)

class Solution:
    def findStrobogrammatic(self, n):
        self.n = n; self.ret = []
        for x in (list("018") if n%2 else [""]):  self.dfs(x)
        return self.ret


    def dfs(self, cur):
        if len(cur)>self.n: return
        if len(cur) == self.n:
            self.ret.append(cur)
            return
        for a,b in '00 11 88 69 96'.split():
            if not (a==b=="0" and len(cur)+2>=self.n): self.dfs(a+cur+b)


'''