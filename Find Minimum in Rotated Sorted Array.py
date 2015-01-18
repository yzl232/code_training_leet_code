# encoding=utf-8
'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
'''
# encoding=utf-8
'''
Find the minimum element in a sorted and rotated array

A sorted array is rotated at some unknown point, find the minimum element in it.

Following solution assumes that all elements are distinct.

Examples

Input: {5, 6, 1, 2, 3, 4}
Output: 1

Input: {1, 2, 3, 4}
Output: 1

Input: {2, 1}
Output: 1

7123456

2345671

最小的元素是唯一一个不满足比前面元素大的。 唯一一个降序
特殊情况是没有rotate。则没有。

A simple solution is to traverse the complete array and find minimum. This solution requires \Theta(n) time.
We can do it in O(Logn) using Binary Search. If we take a closer look at above examples, we can easily figure out following pattern: The minimum element is the only element whose previous element is greater than it. If there is no such element, then there is no rotation and first element is the minimum element. Therefore, we do binary search for an element which is smaller than the previous element.
'''
class Solution:
    # @param num, a list of integer
    # @return an integer   #2345671      7123456
    def findMin(self, arr):  #与arr[h]比较。因为弯折，arr[h]最小。
        ret = arr[0]
        l, h = 0, len(arr)-1  #2345671, 1234567  和arr[l]无法判断，必须arr[h]
        while l<=h:
            m = (l+h)/2   #观察最小1的动向。 rotate到右边了。 与h比较
            ret = min(ret, arr[m])  #与arr[h]比较，同时知道rotate情况。1的情况
            if arr[m]<arr[h]: h = m
            elif arr[m] == arr[h]: h-=1
            else: l=m+1
        return ret
'''
class Solution:
    # @param num, a list of integer
    # @return an integer   #2345671      7123456
    def findMin(self, a):
        l=0; h=len(a)-1
        while l<h and a[l]>=a[h]:  #a[l]<a[h], 那么没有rotate, 直接返回a[l]
            m = (l+h)/2
            if a[m]>a[l]: l=m+1
            elif a[m]<a[l]: h=m
            else: l=l+1
        return a[l]


#leetcode 不重要。accept不重要。关键是背题

s = Solution()
print s.findMin([7 , 2, 3, 4, 5, 6])

'''