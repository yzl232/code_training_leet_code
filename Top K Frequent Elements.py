'''
 Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:

    You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
    Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

'''
class Solution(object):
    def topKFrequent(self, arr, k):  #[1]*n 代表cocatinate n个 [1],  而[]*n  concatinate以后仍然原样。
        ret = []; bucket = [[] for i in range(len(arr))]  #空的[]真没有办法[]*, 是无效的. , 
        for x, freq in collections.Counter(arr).items():   bucket[len(arr) - freq].append(x)
        for x in bucket:
            ret+=x
            if len(ret)>=k: return ret[:k]

'''
class Solution(object):
    def topKFrequent(self, nums, k):
        bucket = [[] for _ in nums]
        for num, freq in collections.Counter(nums).items():
            bucket[len(nums) - freq].append(num)
        return list(itertools.chain(*bucket))[:k]


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