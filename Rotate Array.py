#G家题目。 三次reverse。
'''
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

[show hint]

Related problem: Reverse Words in a String II

Credits:
Special thanks to @Freezen for adding this problem and creating all test cases.

Subscribe to see which companies asked this question
'''

class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n - k-1)
        self.reverse(nums, n - k, n-1)
        self.reverse(nums, 0, n-1)

    def reverse(self, arr, start, end):
        while start<end:  #都是这种限定start, end的reverse
            arr[start], arr[end] = arr[end], arr[start]
            start+=1
            end-=1