'''
 Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

click to show more practice.
More practice:

If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

'''
#和谷歌那道著名的cumulative的sum array挺像的。
#区别：  这个是正数， 大于等于， 用双指针。滑动窗口。  那个是等于， 可以是负数
#以前做过. 搜索sliding  
class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, target, arr):
        ret = float('inf');   s = 0;  l=0
        for r in range(len(arr)):
            s+=arr[r]
            if s>=target:
                while s-arr[l]>=target:
                    s-=arr[l];  l+=1
                ret = min(r-l+1, ret)
        return ret if ret != float('inf') else 0
'''



1) 给个数组seq， 和一个total，找 if there is a contiguous sequence in seq
which sums to total.

也是facebook面经的变体。

geeks也有这道题目


class Solution:
    def print0S(self, arr):  #非常好的代码。    cumulative sum
        d = {0: [-1]}
        s = 0
        for i in range(len(arr)):
            s+=arr[i]
            if s in d:
                for start in d[s]:   print arr[start+1:i+1]  #稍作修改
                d[s].append(i)
            else:  d[s] = [i]      #key是cumulative sum, value index...
s = Solution()
print s.print0S([-1, -3, 4, 5, 4, -2, -2, 0,  4])
'''