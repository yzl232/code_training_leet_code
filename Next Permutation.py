
'''
 Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''
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