'''
 Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, his h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index. 
'''



# encoding=utf-8
'''
Given an unsorted array of integers, you need to return maximum possible n such that the array consists at least n values greater than or equals to n. Array can contain duplicate values.
Sample input : [1, 2, 3, 4] -- output : 2
Sample input : [900, 2, 901, 3, 1000] -- output: 3
'''

#看过2次了

'''
Lets say the array has M numbers. For the purpose of this problem, negative values and 0s are irrelevant. Also, numbers larger than M can be treated as M because the answer is never larger than M.

So, we can count the number of existing values between 1 and M. Then, process the values backwards (M to 1) to find the answer, adding the counts of the values processed so far.

'''
#暴力为O(n2)。 sort为O(nlogn) .  这里空间换时间， 为O(n)
class Solution(object):#和原本array没太大关系 我们建立0~N的cnt  array。 因为结果可能是0~N。
    def hIndex(self, vals):#返回的n是数目， 实际上处于0~n之间。  这样子要大于等于n。 我们忽略负数.
        n = len(vals); curN=0; cnt = [0]*(n+1) #cnt[i] cnt数目。
        for x in vals:  cnt[max(0, min(n, x))] +=1  #大于等于n的视为n  # ignore negative values
        for i in range(len(cnt)-1, -1, -1):   # 0~n  为了对应cnt array
            curN +=cnt[i]  #非常巧妙
            if curN>=i:  return i
        return 0          #也可以用counting sort。   然后sort。     
#返回的值， 都是从n, n-1, ...2, 1, 0
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