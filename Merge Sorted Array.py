class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        pa = m-1; pb = n-1
        while pa>=0 and pb>=0:
            if A[pa] > B[pb]:
                A[pa+pb+1] = A[pa]
                pa -=1
            else:
                A[pa+pb+1] = B[pb]
                pb -=1
        while pb>=0:
            A[pb] = B[pb]
            pb-=1