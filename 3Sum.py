'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

    Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
    The solution set must not contain duplicate triplets.

    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
'''


class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num.sort()
        res = set()
        for i in range(len(num)-2):
            if i>0 and num[i] == num[i-1]: continue
            left = i+1; right = len(num)-1; target = 0 - num[i]
            while left < right:
                if num[left] + num[right] == target:
                    res.add((num[i], num[left], num[right]))
                    left+=1; right -=1
                elif num[left] + num[right] < target:
                    left+=1
                else:
                    right -=1
        return [list(i) for i in res]
        
'''
class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num.sort()
        d, result = {}, set()
        for i in range(len(num)):
            for j in range(i+1, len(num)):
                if num[i] + num[j] not in d:  d[num[i] + num[j]] = [[num[i], num[j]]]
                else: d[num[i] + num[j]].append([num[i], num[j]])
        for i in range(len(num)-2):
            target = 0-num[i]
            if target in d:
                for k in d[target]:
                    if num[k[0]]>=num[i]:
                        result.add((num[i], k[0], k[1] ))
        return [list(i) for i in result]
'''