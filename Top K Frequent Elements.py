'''
 Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:

    You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
    Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

'''
# hashtable + (bucket sort or quick select)
class Solution(object):
    def topKFrequent(self, nums, k):
        bucket = [[] for _ in nums]
        for x, freq in collections.Counter(nums).items():   bucket[len(nums) - freq].append(x)
        ret = []
        for x in bucket:
            if len(x)>=k: return ret+x[:k]
            ret+=x;  k-=len(x)
        return ret
'''
class Solution(object):
    def topKFrequent(self, nums, k):
        bucket = [[] for _ in nums]
        for num, freq in collections.Counter(nums).items():
            bucket[len(nums) - freq].append(num)
        return list(itertools.chain(*bucket))[:k]
'''