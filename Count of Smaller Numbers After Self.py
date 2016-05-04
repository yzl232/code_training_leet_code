 You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

Return the array [2, 1, 1, 0]. '''



'''

#有点像G家题 Count Inversions in an array 同一思想。  
# https://leetcode.com/discuss/73509/nlogn-time-space-mergesort-solution-with-detail-explanation

class Solution:
    def countSmaller(self, nums):
        def mSort(arr):
            if len(arr)<=1: return arr
            l, r = mSort(arr[:len(arr) / 2]), mSort(arr[len(arr) / 2:])
            for i in xrange(len(arr)-1, -1, -1):   #merge
                if not r or (l and l[-1][1] > r[-1][1]):
                    ret[l[-1][0]] += len(r)# 和inversion一样， 都是加上l, 或r的 右边一部分的长度
                    arr[i] = l.pop()
                else:  arr[i] = r.pop()
            return arr
        ret = [0] * len(nums)
        mSort(list(enumerate(nums)))
        return ret
#比较tricky的题目。 类似以前count inversion的题目.    但不是总数， 是每个的inversion数目都计算。    而且是计算比自己小的数， 于是必须反向。
# 可以计算surpass.   处理一下得到。
#不过会代码长， 还是用stepha你的代码。
