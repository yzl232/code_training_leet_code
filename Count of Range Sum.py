'''

 Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:
Given nums = [-2, 5, -1], lower = -2, upper = 2,
Return 3.
The three ranges are : [0, 0], [2, 2], [0, 2] and their respective sums are: -2, -1, 2. 
'''


#挺名字就很适合binary indexed tree.   range sum
class Solution(object):  #  merge sort
    def countRangeSum(self, nums, lower, upper):
        accu = [0]
        for num in nums:  accu.append(accu[-1] + num)
        def mSort(l, h):
            m = (l + h) / 2
            if m == l:  return 0
            count = mSort(l, m) + mSort(m, h)
            i = j = m
            for left in accu[l:m]:
                while i < h and accu[i] - left <  lower: i += 1
                while j < h and accu[j] - left <= upper: j += 1
                count += j - i
            accu[l:h] = sorted(accu[l:h])  # 他这里完全没有merge啊.   
            return count
        return mSort(0, len(accu))
     
'''
def countRangeSum(self, nums, lower, upper):
    n = len(nums)
    Sum, BITree = [0] * (n + 1), [0] * (n + 2)

    def count(x):
        s = 0
        while x:
            s += BITree[x]
            x -= (x & -x)
        return s

    def update(x):
        while x <= n + 1:
            BITree[x] += 1
            x += (x & -x)

    for i in range(n):
        Sum[i + 1] = Sum[i] + nums[i]
    sortSum, res = sorted(Sum), 0
    for sum_j in Sum:
        sum_i_count = count(bisect.bisect_right(sortSum, sum_j - lower)) - count(bisect.bisect_left(sortSum, sum_j - upper))
        res += sum_i_count
        update(bisect.bisect_left(sortSum, sum_j) + 1)
    return res

'''