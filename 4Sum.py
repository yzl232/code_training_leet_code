'''
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

    Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
    The solution set must not contain duplicate quadruplets.

    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)

'''
class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        n = len(num);    res = set()
        d = {};   num.sort()
        for p in range(n):
            for q in range(p+1, n):
                if num[p] + num[q] not in d:       d[ num[p] + num[q] ] = []
                d[ num[p] + num[q] ].append((p, q))
        for i in range(n):
            for j in range(i+1, n - 2):
                t = target - num[i] - num[j]  #i, j是最左边的。
                if t in d:
                    for k in d[t]:  #hashtable是右边的
                        if k[0] > j:       res.add( (num[i], num[j], num[k[0]], num[k[1]]) )
        return  [list(i) for i in res]