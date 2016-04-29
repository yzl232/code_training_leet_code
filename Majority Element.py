'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Credits:
'''

class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, arr):
        maj = self.findCandidate(arr)
        assert arr.count(maj)>len(arr)/2
        return maj    
    
    def findCandidate(self, arr):
        ret =arr[0]; cnt=0
        for x in arr:
            if x==ret: cnt+=1
            else: cnt-=1
            if cnt==0:  #之前部分没有出现超过半数的元素。 继续到剩下的部分找。
                ret=x;  cnt=1
        return ret
        



'''
 现在来分析一下复杂度。删除元素可以在常数时间内完成，但找不同元素似乎有点麻烦。实际上，我们可以换个角度来想，用一个小trick来重新实现下该算法。

在算法执行过程中，我们使用常量空间实时记录一个候选元素c以及其出现次数f(c)，c即为当前阶段出现次数超过半数的元素。在遍历开始之前，该元素c为空，f(c)=0。然后在遍历数组A时，

    如果f(c)为0，表示当前并没有候选元素，也就是说之前的遍历过程中并没有找到超过半数的元素。那么，如果超过半数的元素c存在，那么c在剩下的子数组中，出现次数也一定超过半数。因此我们可以将原始问题转化为它的子问题。此时c赋值为当前元素, 同时f(c)=1。
    如果当前元素A[i] == c, 那么f(c) += 1。(没有找到不同元素，只需要把相同元素累计起来)
    如果当前元素A[i] != c，那么f(c) -= 1 (相当于删除1个c)，不对A[i]做任何处理(相当于删除A[i])

如果遍历结束之后，f(c)不为0，那么再次遍历一遍数组，记录c真正出现的频率，从而验证c是否真的出现了超过半数。上述算法的时间复杂度为O(n)，而由于并不需要真的删除数组元素，我们也并不需要额外的空间来保存原始数组，空间复杂度为O(1)。实际上，在Moore大牛的主页上有针对这个算法的一个演示，感兴趣的同学可以直接移步观看。


Check for Majority Element in a sorted array

Question: Write a C function to find if a given integer x appears more than n/2 times in a sorted array of n integers.

Basically, we need to write a function say isMajority() that takes an array (arr[] ), array’s size (n) and a number to be searched (x) as parameters and returns true if x is a majority element (present more than n/2 times).


sorted显然用binary search
class Solution:
    def isMajority(self, arr, x):
        n = len(arr); i = self.bs(arr, x); end = i+n/2
        return i!=-1 and end<=n-1 and arr[end]==x

    def bs(self, arr, x):
        l=0; h = len(arr)-1
        while l<=h:
            m = (l+h)/2
            if (m==0 or arr[m-1]!=x) and arr[m]==x: return m
            elif arr[m]<x: l = m+1
            else:  h=m-1    #其他时候，相等的时候，也是在左边
        return -1
'''