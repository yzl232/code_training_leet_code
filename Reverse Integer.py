class Solution:
    # @return an integer
    def reverse(self, x):
        if x > 0: 
            s = str(x)
            return int(s[::-1])
        s = str(0-x)
        return 0-int(s[::-1])