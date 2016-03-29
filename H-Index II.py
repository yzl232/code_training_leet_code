'''
ollow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm? 
'''
#  [2, 3, 5, 9]   arr[i]<(n-i): return n-i-1
# [4, 3, 1, 0]   arr[i]<i+1   : return i
#[1]
class Solution(object):
    def hIndex(self, citations):  # sorted  80%考binary search
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        l, h = 0, n-1
        while l<=h:
            m = (l+h)/2
            if n-m > citations[m]: l=m+1   #没有那么多。 往右靠。
            else:  h= m-1  #因为m不满足. 所以+1, -1
        return n-l
'''
ust binary search, each time check citations[mid] case 1: citations[mid] == len-mid, then it means there are citations[mid] papers that have at least citations[mid] citations. case 2: citations[mid] > len-mid, then it means there are citations[mid] papers that have moret than citations[mid] citations, so we should continue searching in the left half case 3: citations[mid] < len-mid, we should continue searching in the right side After iteration, it is guaranteed that right+1 is the one we need to find (i.e. len-(right+1) papars have at least len-(righ+1) citations)
'''