class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        n = len(num)
        for i in range(n-1, 0, -1):
            if num[i] > num[i-1]:
                small = i
                for j in range(i+1, n):
                    if num[j] < num[small] and num[j] > num[i-1]:
                        small = j
                num[small], num[i-1] = num[i-1], num[small]
                temp = num[i:]
                temp.sort()
                return num[:i] + temp
        return num[::-1]