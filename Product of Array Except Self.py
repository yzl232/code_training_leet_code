'''
 Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)
'''
class Solution(object):
    def productExceptSelf(self, arr):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cur=1; ret =[1]*len(arr)
        for i in range(len(arr)):
            ret[i]*=cur
            cur *=arr[i]  # cur放在后面
        cur = 1
        for i in range(len(arr)-1, -1, -1):
            ret[i]*=cur
            cur *=arr[i]
        return ret