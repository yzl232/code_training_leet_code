class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ones = 0; twos = 0; threes = 0
        for i in A:
            twos |= ones & i
            ones ^= i
            threes = ones & twos
            ones &= ~threes
            twos &= ~threes
        return ones