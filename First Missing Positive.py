class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, a):
        n = len(a)
        i = 0
        while i<n:
            if a[i] > 0 and a[i] < n+1 and a[i] != a[a[i]-1] and a[i]!=i+1:
                temp = a[i]-1
                a[i], a[temp] = a[temp], a[i]
            else: i+=1
        
        for i in range(n):
            if a[i] != i+1:
                return i+1
        return n+1