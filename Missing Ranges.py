# encoding=utf-8
'''
 Given a sorted integer array where the range of elements are [lower, upper] inclusive, return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].
'''
class Solution:
    # @param A, a list of integers
    # @param lower, an integer
    # @param upper, an integer
    # @return a list of strings
    def findMissingRanges(self, vals, start, end ):  # 就是比较邻居的差值。
        ret=[]; vals = [start-1]+vals+[end+1]   #补上两个多余的量。 来处理边界
        for i in range(len(vals)-1):
            a = vals[i]+1; b=vals[i+1]-1
            if a<=b: ret.append(self.help(a, b))
        return ret

    def help(self, l, r):
        return str(l) if l==r else str(l)+'->'+str(r)