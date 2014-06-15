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