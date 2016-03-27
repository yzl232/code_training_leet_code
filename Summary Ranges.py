'''
 Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"]. 
'''

class Solution(object):
    def summaryRanges(self, nums):
        ranges = []
        for x in nums:
            if not ranges or x > ranges[-1][-1] + 1:  ranges.append([])
            ranges[-1][1:] = [x]
        return ['->'.join(map(str, r)) for r in ranges]   # map here:  an array of ints to an array of strings