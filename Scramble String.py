class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        if s1 == s2: return True
        n1 = len(s1); n2 = len(s2)
        if n1 != n2: return  False
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