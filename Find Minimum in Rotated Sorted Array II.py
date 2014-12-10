# encoding=utf-8
'''
    Follow up for "Find Minimum in Rotated Sorted Array":
    What if duplicates are allowed?

    Would this affect the run-time complexity? How and why?

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
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
    def findMin(self, a):
        l=0; h=len(a)-1
        while l<h and a[l]>=a[h]:
            m = (l+h)/2
            if a[m]>a[l]: l=m+1
            elif a[m]<a[l]: h=m
            else: l=l+1
        return a[l]


#leetcode 不重要。accept不重要。关键是背题

s = Solution()
print s.findMin([7 , 2, 3, 4, 5, 6])

