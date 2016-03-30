'''


    Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

    For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].

'''

class Solution:
    def wiggle(self, arr):
        for i in range(1, len(arr)):
            if (i&1 and arr[i] < arr[i-1])  or (not (i&1) && arr[i] > arr[i-1]):
                arr[i], arr[i-1] = arr[i-1], arr[i]
        