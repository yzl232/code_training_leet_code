'''
 Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
'''

class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        d = {x:False for x in num} # False means not visited
        ret = 0
        for x in d:
            if not d[x]:
                a = x + 1;  b = x - 1
                while a in d and not d[a]:
                    d[a] = True; a += 1
                while b in d and not d[b]:
                    d[b] = True; b -= 1
                ret = max(ret, a-b-1)
        return ret
#  上面这个简单。  是2 pass
#  下面这个是one pass. 不过难一些。
#区别不大。 还是用原来的吧~~
'''
class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        d={};  ret=0
        for x in num:
            if x in d: continue
            l, r= d.get(x-1, 0), d.get(x+1, 0)
            ret = max(ret, l+r+1)
            d[x]=d[x-l]=d[x+r]=l+r+1
        return ret
#  https://oj.leetcode.com/discuss/18886/my-really-simple-java-o-n-solution-accepted
'''