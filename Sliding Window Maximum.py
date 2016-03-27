'''
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Therefore, return the max sliding window as [3,3,5,5,6,7].
'''

# Removing redundant elements and storing only elements that need to be considered in the queue is the key to achieve the efficient O(n) solution below.
#想，一个值比较旧，来了比它大的新值之后，它永远不会是窗口内最大值了，这种没前途的值就没必要存了……
#所以当来一个新值的时候，我们把队尾这端的不大于它（小于或等于）的值都踢出去，再把这个值入队

# 和那道题用stack求next greater number 很像的。 基本一样。就是最大q[0]. q的最左边。 stack最大的是arr[i].栈的顶部  for循环里边就2行。
from collections import deque
class Solution:  #去年做过
    # @param {integer[]} nums     #从队尾pop, 就是考虑到if q[0] == i - k:    q.popleft()
    # @param {integer} k
    # @return {integer[]}
    def maxSlidingWindow(self, nums, k):  # 双端队列
        q = deque()
        ret = []
        for i in range(len(nums)):
            while q and nums[q[-1]] <= nums[i]:  q.pop()
            q.append(i)
            if q[0] == i - k:    q.popleft()
            if i >= k - 1:    ret.append(nums[q[0]])
        return ret
#http://bookshadow.com/weblog/2015/07/18/leetcode-sliding-window-maximum/