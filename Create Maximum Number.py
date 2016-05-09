'''
 Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length k <= m + n from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the k digits. You should try to optimize your time and space complexity.

Example 1:

nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
return [9, 8, 6, 5, 3]

Example 2:

nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
return [6, 7, 6, 0, 4]

Example 3:

nums1 = [3, 9]
nums2 = [8, 9]
k = 3
return [9, 8, 9] 
'''

class Solution(object):
    def maxNumber(self, a, b, k):
        def prep(arr, k):
            drop = len(arr) - k; ret = []
            for x in arr:  #很巧妙, 利用了drop = len(arr) - k.  这样从最开始就可以pop了.
                while drop>0 and ret and ret[-1] < x:
                    ret.pop(); drop -= 1 # #有点像maximum rectangle。  尽量保持out最大。 #也像next greater number
                ret.append(x)
            return ret[:k]
        def merge(a, b): return [max(a, b).pop(0) for _ in a+b]
        return max(merge(prep(a, i), prep(b, k - i)) for i in range(k + 1) if i <= len(a) and k - i <= len(b))
#突然就解决了rocket fuel的题  