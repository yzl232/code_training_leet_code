class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        n = len(s)
        b = [False]*(n+1)
        b[0] = True
        for i in range(1, n+1):
            current_s = s[:i]
            for j in range(0, i):
                word = s[j:i]
                if b[j] and (word in dict) :
                    b[i] = True
                    break

        #print b
        return b[n]
