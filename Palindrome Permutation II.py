# encoding=utf-8

'''
Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

For example:

Given s = "aabb", return ["abba", "baab"].

Given s = "abc", return [].

Hint:

    If a palindromic permutation exists, we just need to generate the first half of the string.
    To generate all distinct permutations of a (half of) string, use a similar approach from: Permutations II or Next Permutation.
'''
class Solution(object):
    def generatePalindromes(self, s):
        d = collections.Counter(s)
        m = [k for k in d if d[k] % 2]
        s =  ''.join(k*(d[k]/2) for k in d)
        return [] if len(m)>1 else [''.join(list(x) + m + list(x)[::-1]) for x in set(itertools.permutations(s))]
        
#下面这个好像可以。
'''
class Solution(object):
    def generatePalindromes(self, s):
        d = collections.Counter(s)
        m = ''.join([k for k in d if d[k] % 2])
        s =  ''.join(k*(d[k]/2) for k in d)
        return [] if len(m)>1 else [x + m + x[::-1] for x in set(itertools.permutations(s))]
'''        

'''

class Solution(object):
    def generatePalindromes(self, s):
        d = collections.Counter(s)
        mid = [k for k in d if d[k] % 2]
        p = list(''.join(k*(d[k]/2) for k in d))  #出现奇数次的话, 除以2正好
        return [''.join(i + mid + i[::-1]) for i in self.permuteUnique(p)] if len(mid) <=1 else []

    def permuteUnique(self, arr):
        arr.sort()
        self.ret = []
        self.dfs([], arr)
        return self.ret

    def dfs(self, cur, arr):
        if not arr:
            self.ret.append(cur)
            return
        for i in xrange(len(arr)):
            if i>0 and arr[i] == arr[i-1]: continue
            t = arr[:]
            self.dfs(cur+[t.pop(i)], t)
'''