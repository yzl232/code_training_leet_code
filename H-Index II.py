'''
ollow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm? 
'''

class Solution(object):
    def hIndex(self, arr):  # sorted  80%考binary search
        n = len(arr);   l, h = 0, n-1
        while l<=h:
            m = (l+h)/2
            if arr[m]<n-m: l= m + 1 #没有那么多。 往右靠。
            else:  h= m-1    #因为m不满足. 所以+1, -1
        return n-l

#类似搜索左边界.  就是搜索满足第一个满足 arr[i]>=n-i

'''
排序做法
def hIndex(self, citations):
    citations.sort()
    n = len(citations)
    for i in xrange(n):
        if citations[i] >= (n-i):
            return n-i
    return 0
'''
