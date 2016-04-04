#https://www.hrwhisper.me/binary-indexed-tree-fenwick-tree/
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.sums = [0] * (len(nums) + 1)
        self.nums = nums
        self.n = len(nums)
        for i in xrange(len(nums)):
            self.update(i + 1,nums[i])

    def sum(self,x):
        res = 0
        while x:
            res += self.sums[x]
            x -=  (x & -x)
        return res

    def update(self, x , val):
        self.nums[x-1] = val
        while x <= self.n:
            self.sums[x] += val - self.nums[x]
            x += (x & -x)

    def sumRange(self, i, j):
        if not self.nums: return  0
        return self.sum(j+1) - self.sum(i)


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)