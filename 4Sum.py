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
        num.sort()
        l = len(num)
        ret = set()
        d = {}
        for i in range(l-1):
            for j in range(i+1, l):
                if (num[i] + num[j]) not in d:
                    d[num[i] + num[j]] = [(i, j)]
                else:
                    d[num[i] + num[j]].append((i, j))
        for i in range(l-3):
            for j in range(i+1, l-2):
                remain = target- num[i] - num[j]
                if remain in d:
                    for k in d[remain]:
                        if j<k[0]:
                            ret.add((num[i], num[j], num[k[0]], num[k[1]]))
        return [list(i) for i in ret]