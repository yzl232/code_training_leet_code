# encoding=utf-8
import heapq
'''
 city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).
Buildings Skyline Contour

The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

    The number of buildings in any input list is guaranteed to be in the range [0, 10000].
    The input list is already sorted in ascending order by the left x position Li.
    The output list must be sorted by the x position.
    There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]

'''
class Solution:  # http://www.cnblogs.com/easonliu/p/4531020.html
    # @param {integer[][]} buildings  # float("inf"), float("-inf")
    # @return {integer[][]}   #那就是把左边节点的高度值设成负数，右边节点的高度值是正数，这样我们就不用额外的属性，
    def getSkyline(self, blds):
        arr = sorted([(l, -h, r) for l, r, h in blds] + [(r, 0, None) for l, r, h in blds])
        ret, heap = [[0, 0]], [(0, float("inf"))]    # r是正常的排序.  就是h排序相反.嗯.
        for x, h, r in arr:
            while x >= heap[0][1]:  heapq.heappop(heap)   #当超过了heap最大的节点的右边界.  #不断pop。 知道最大节点右边界大于x
            if h:   heapq.heappush(heap, (h, r))
            if ret[-1][1] + heap[0][0]:  ret.append([x, -heap[0][0]]) #不相同高度.  相同高度不管.
        return ret[1:]
'''
s = Solution()
print s.getSkyline([ [2 ,9, 10], [3, 7, 15], [5, 12, 12]])
'''