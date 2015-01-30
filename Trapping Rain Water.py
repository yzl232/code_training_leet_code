'''
 Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6....
'''



class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, arr): # http://yucoding.blogspot.com/2013/05/leetcode-question-111-trapping-rain.html
        l=0; r=len(arr)-1
        ret = maxL=maxR=0
        while l<r:
            maxL = max(maxL, arr[l])
            maxR = max(maxR, arr[r])
            if arr[l]<=arr[r]:   #由左边决定
                ret+=maxL-arr[l]
                l+=1
            else:   #由右边决定
                ret +=maxR-arr[r]
                r-=1
        return ret
# one    pa s s     O(1) space
#l, r这个东西很管用。 哪个更大，l, r就不会动了。


'''
如果哪一侧的高度是小的，那么从这里开始继续扫，如果比它还小的，肯定装水的瓶颈就是它了，可以把装水量加入结果，如果遇到比它大的，立即停止，重新判断左右窗口的大小情况，重复上面的步骤。这里能作为停下来判断的窗口，说明肯定比前面的大了，所以目前肯定装不了水（不然前面会直接扫过去）。这样当左右窗口相遇时，就可以结束了，因为每个元素的装水量都已经记录过了
'''

#l我们要求的是l, r之间的部分。  l左边， r右边的已经搞定了。。
# Because the volume always depends on the shorter bar.

'''
class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, arr): # http://yucoding.blogspot.com/2013/05/leetcode-question-111-trapping-rain.html
        n = len(arr); ret = 0
        l = [0 for i in range(n)];  r =l[:]
        for i in range(1, n-1):    l[i] = max(l[i-1], arr[i-1])
        for i in range(n-2, 0, -1):    r[i] = max(r[i+1], arr[i+1])
        for i in range(1, n-1):  ret += max(  min(l[i], r[i])-arr[i],   0)
        return ret
'''