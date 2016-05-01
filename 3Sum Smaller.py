'''

Problem Description:

Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

For example, given nums = [-2, 0, 1, 3], and target = 2.

Return 2. Because there are two triplets which sums are less than 2:

[-2, 0, 1]
[-2, 0, 3]

Follow up:
Could you solve it in O(n^2) runtime?
'''

class Solution:
    def threeSumSmaller(self, arr, x):
        arr.sort();  cnt = 0
        for k in range(len(arr)):
            i, j = k + 1, len(arr) - 1
            while i<j:
                if arr[i] + arr[j] + arr[k] < x:
                    cnt += j-i;   i+=1
                else:   j -= 1
        return cnt