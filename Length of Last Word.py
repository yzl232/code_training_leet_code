class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        s1 = s.split()
        if s1 == []: return 0
        return len(s1[-1])
        