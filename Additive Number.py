'''
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

For example:
"112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.

1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

"199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.

1 + 99 = 100, 99 + 100 = 199

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Follow up:
How would you handle overflow for very large input integers? 
'''


class Solution(object):
    def isAdditiveNumber(self, s):
        return self.dfs(s, 0, None, None)

    def dfs(self, s, n, x1, x2):      # x is the size
        if not s: return n >= 3
        return any((i==1 or s[0]!="0") and (x1==None or x2==None or int(s[:i]) == x1 + x2) and self.dfs(s[i:], n + 1, x2, int(s[: i])) for i in range(1, len(s) + 1))

#        return n >= 3 if not s else any((i==1 or s[0]!="0") and (x1==None or x2==None or int(s[:i]) == x1 + x2) and self.dfs(s[i:], n + 1, x2, int(s[: i])) for i in range(1, len(s) + 1))

'''

class Solution(object):
    def isAdditiveNumber(self, num, i=0, n=1, pre2=None, pre1=None):
        if i == len(num): return n > 3
        for size in range(1, len(num)-i+1):
            if size > 1 and num[i] == '0': return False
            v = int(num[i: i+size])
            if (n <= 2 or v == pre2 + pre1) and self.isAdditiveNumber(num, i+size, n+1, pre1, v): return True
        return False

n means the nth number to process, only numbers after 2nd number should be checked by the additive number rule:

1st + 2nd = 3rd
2nd + 3rd = 4th
3rd + 4th = 5th
...

which is implemented as:

if n > 2 and not v == pre2 + pre1: continue

class Solution(object):
    def isAdditiveNumber(self, s):
        return self.dfs(s, 1, None, None)

    def dfs(self, s, n, pre2, pre1):      # x is the size
        if not s: return n > 3
        return any(not (i > 1 and s[0] == '0') and (n <= 2 or int(s[:i]) == pre2 + pre1) and self.dfs(s[i:], n + 1, pre1, int(s[: i])) for i in range(1, len(s)+ 1))


class Solution(object):
    def isAdditiveNumber(self, num):
        if not num or len(num) < 3:  return False
        n = len(num)
        for i in range(1, n):
            if i > 1 and num[0] == '0':   break
            for j in range(i+1, n):
                a, b, c = 0, i, j
                if num[b] == '0' and c > b + 1:   break
                while c < n:
                    ret = str(int(num[a:b]) + int(num[b:c]))
                    if num[c:].startswith(ret):  a, b, c = b, c, c + len(ret)
                    else:  break
                if c == n: return True
        return False
'''