'''
 Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, his h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index. 
'''

class Solution(object):
    def hIndex(self, vals):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(vals); curN=0
        cnt = [0]*(n+1) #cnt[i] cnt数目。
        for x in vals:
            if x>=n:  cnt[n]+=1   #大于等于n的视为n
            elif x>=0: cnt[x]+=1   # ignore negative values
        for i in range(len(cnt)-1, -1, -1):   # 0~n  为了对应cnt array
            curN +=cnt[i]  #非常巧妙
            if curN>=i:  return i
        return 0