'''
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''


class Solution:  #那个majority也有用到。
    def leftS(self, arr, x):
        l=0; h = len(arr)-1
        while l<=h:
            m = (l+h)/2
            if (m==0 or arr[m-1]<x) and arr[m]==x: return m
            elif arr[m]<x: l = m+1
            else:  h=m-1    #其他时候，相等的时候，也是在左边
        return -1

    def rightS(self, arr, x):
        l=0; h = len(arr)-1
        while l<=h:
            m = (l+h)/2
            if (m==len(arr)-1 or arr[m+1]>x) and arr[m]==x: return m
            elif arr[m]<=x: l = m+1   #其他时候，相等的时候，也是在右边
            else:  h=m-1
        return -1

    def searchRange(self, arr, x):
        return [self.leftS(arr,x), self.rightS(arr,x)]

'''
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        l, h = 0, len(A)-1
        result = [-1, -1]    #在二分查找到元素时，需要向前和向后遍历来找到target元素的起点和终点。
        while l<=h:
            m = (l+h)/2
            if A[m] > target: h = m-1
            elif A[m]<target: l = m+1
            else:
                result[0], result[1] = m, m
                i = m-1
                while i>=0 and A[i] == target:
                    result[0] = i
                    i-=1
                i = m+1
                while i<len(A) and A[i] == target:
                    result[1] = i
                    i+=1
                return result
        return result
'''