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
    def fourSum(self, arr, target):
        n = len(arr);    ret = set()
        d = {};   arr.sort()
        for i in range(n):
            for j in range(i+1, n):
                s = arr[i] + arr[j]
                if s not in d:   d[ s ] = []
                d[ s ].append((i, j))
        for i in range(n):
            for j in range(i+1, n - 2):
                s = target - arr[i] - arr[j]  #i, j是最左边的。
                if s in d:
                    for k in d[s]:  #hashtable是右边的
                        if k[0] > j:       ret.add( (arr[i], arr[j], arr[k[0]], arr[k[1]]) )
        return  [list(i) for i in ret]