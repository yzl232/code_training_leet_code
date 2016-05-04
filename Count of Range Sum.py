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
        first = [0]
        for num in nums:  first.append(first[-1] + num)
        def mSort(l, h):
            m = (l + h) / 2
            if m == l:  return 0
            count = mSort(l, m) + mSort(m, h);  i = j = m
            for left in first[l:m]:
                while i < h and first[i] - left <  lower: i += 1
                while j < h and first[j] - left <= upper: j += 1
                count += j - i
            first[l:h] = sorted(first[l:h])
            return count
        return mSort(0, len(first))
        
'''
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        if not nums:
            return 0

        n = len(nums)
        if n == 1:
            return int(lower <= nums[0] <= upper)

        mid = n >> 1
        count = sum([
            self.countRangeSum(array, lower, upper)
            for array in [nums[:mid], nums[mid:]]
        ])

        suffix, prefix = [0] * (mid + 1), [0] * (n - mid + 1)
        for i in xrange(mid - 1, -1, -1):
            suffix[i] = suffix[i + 1] + nums[i]

        for i in xrange(mid, n):
            prefix[i - mid + 1] = prefix[i - mid] + nums[i]

        suffix, prefix = suffix[:-1], sorted(prefix[1:])
        count += sum([
            bisect.bisect_right(prefix, upper - s) -
            bisect.bisect_left(prefix, lower - s)
            for s in suffix
        ])

    return count


'''