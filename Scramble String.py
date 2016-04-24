
'''
 Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t

To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t

We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a

We say that "rgtae" is a scrambled string of "great".

'''

class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        if s1 == s2: return True
        if len(s1) != len(s2) or sorted(s1) != sorted(s2): return False
        return any((self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or (self.isScramble(s1[:i], s2[len(s1)-i:]) and self.isScramble(s1[i:], s2[:len(s1)-i]))  for i in range(1, len(s1)))
'''
class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        if s1 == s2: return True
        n1 = len(s1); n2 = len(s2)
        if n1 != n2: return  False
        if sorted(s1)!= sorted(s2): return False
        f = {}
        for i in range(n1):
            for j in range(n1):
                f[i, j, 0] = True    # empty string
                f[i, j, 1] = (s1[i] == s2[j])

        for n in range(2, n1+1):
            for i in range(n1-n+1):
                for j in range(n1-n+1):  # 0 ~  n1-k.... n1-1
                    f[i, j, n] = False
                    for m in range(1, n):  # for all the possible m. Check if it is True
                        f[i, j, n] = (f[i, j, m] and f[i+m, j+m, n-m]) or (f[i, j+n-m, m] and f[i+m, j, n-m]) # It will be fine since n from 2 => n.       All these parameters in the transition function are less than n
                        if f[i, j, n]: break
        return f[0, 0, n1]
'''