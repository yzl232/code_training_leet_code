'''
An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The black pixels are connected, i.e., there is only one black region. Pixels are connected horizontally and vertically. Given the location (x, y) of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

For example, given the following image:

[
  "0010",
  "0110",
  "0100"
]

and x = 0, y = 2,

Return 6.
'''
class Solution:  # algorithm runs in O(m log n + n log m)
    def minArea(self, grid, x, y):   #原点在左上角. 和matrix 的index一致的.
        def search(l, h, check):  #该函数返回最靠左的满足check的index
            while l <= h:
                m = (l + h) / 2
                if l==h: return m
                if check(m):  h = m #满足的话, mid可能是.
                else:   l = m + 1  #不满足. mid不可能是   #使用len(grid)而非len(grid)-1主要考虑没搜索到时, 且len(grid)-1那行也没有, 边界结果应返回len(grid)-1
        r1, r2 = search(0, x, lambda i: '1' in grid[i]), search(x + 1, len(grid), lambda i: '1' not in grid[i])  #边界+1
        c1, c2 = search(0, y, lambda j: "1" in [grid[i][j] for i in range(r1, r2)]), search(y + 1, len(grid[0]), lambda j: "1" not in [grid[i][j] for i in range(r1, r2)])    #边界+1
        return (c2 - c1) * (r2 - r1)  #直接range(len(image))也一样的.    
        
#从图中的例子看， 边界也可以代替0来包围。
'''
O(m*n)解法：
class Solution:  # algorithm runs in O(m log n + n log m)
    def minArea(self, image, x, y):
        return sum('1' in r for r in image) * sum('1' in c for c in zip(*image))

'''