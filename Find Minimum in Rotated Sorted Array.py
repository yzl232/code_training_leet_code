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

1234567
三个极端例子足够了。
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


# encoding=utf-8



Find the maximum element in an array which is first increasing and then decreasing

Given an array of integers which is initially increasing and then decreasing, find the maximum value in the array.

Input: arr[] = {8, 10, 20, 80, 100, 200, 400, 500, 3, 2, 1}
Output: 500

Input: arr[] = {1, 3, 50, 10, 9, 7, 6}
Output: 50

Corner case (No decreasing part)
Input: arr[] = {10, 20, 30, 40, 50}
Output: 50

Corner case (No increasing part)
Input: arr[] = {120, 100, 80, 20, 0}
Output: 120
这道题目就是rotated的变种。
但是不完全一样，有变小的递减部分。
rotate没有递减。

2345671
67123456
                   #7123456     2345671


#if h==l+1:  return max(arr[l], arr[h])    #主要是解除了m-1, m+1超过了边界的情况

#binary search的题目就是要举例子，来判断if  else


#虽然和rotated的题目略不同。 输入不同。 但是代码完全可以用
#因为最大总是在相对中间的位置


#下面这个是rotated array的maximum。
#照抄leetcode minimum试试
# 对比leetcode以后， 可以得出结论。
class Solution:
    # @param num, a list of integer
    # @return an integer   #2345671      7123456
    def findMax(self, arr):
        ret = arr[0]
        l, h = 0, len(arr)-1   #7123456, 1234567  和arr[h]无法判断，必须arr[h]
        while l<=h:     #记忆方法，7的位置，rotate时在左边， 与左边比较。
            m = (l+h)/2  #与arr[l]比较，可以同时知道rotate情况与max.
            ret = max(ret, arr[m])
            if arr[m]>arr[l]: l=m
            elif arr[m]==arr[l]: l+=1
            else: h=m-1  #这道题，这里可以 return arr[l]
        return ret

s = Solution()
print s.findMax([1, 5 , 7, 14 , 2, 1])
print s.findMax([1, 3, 4, 7, 9])
print s.findMax([7, 4, 2])

class Solution:
    def findMax(self, arr):
        l =0;  h=len(arr)-1
        while l<=h:
            if h<=l+1:  return max(arr[l], arr[h])  #主要是解除了m-1, m+1超过了边界的情况.   因为是求max。 才能这样搞。
            m = (l+h)/2
            if arr[m]>arr[m-1] and arr[m]>arr[m+1]: return arr[m]  #主要的比较部分涉及三个数。  所以之前考虑特殊的只有2个数情况
            elif arr[m-1]>arr[m]>arr[m+1]:  h = m-1      #递减部分,最大在左边
            else: l = m+1 #递增部分

s = Solution()
print s.findMax([1, 5 , 7, 14 , 2, 1])
print s.findMax([1, 3, 4, 7, 9])
print s.findMax([7, 4, 2])

'''







