'''
 Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"]. 
'''

class Solution(object):
    def summaryRanges(self, nums):
        ranges = []
        for x in nums:
            if not ranges or x > ranges[-1][-1] + 1:  ranges.append([x])
            else: ranges[-1] = [ranges[-1][0], x] 
        return ['->'.join([str(x) for x in r]) for r in ranges]
'''
class Solution(object):
    def summaryRanges(self, nums):
        ranges = []
        for n in nums:
            if not ranges or n > ranges[-1][-1] + 1:  ranges.append([])
            ranges[-1][1:] = [n]  #比较巧妙，保证了len为1 或者2.
        return ['->'.join(map(str, r)) for r in ranges]
'''