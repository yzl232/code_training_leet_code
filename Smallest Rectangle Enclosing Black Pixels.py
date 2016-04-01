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
    def minArea(self, image, x, y):   #原点在左上角. 和matrix 的index一致的.
        top = self.search(0, x, lambda i: '1' in image[i])
        bottom = self.search(x + 1, len(image), lambda i: '1' not in image[i])  #边界+1
        left = self.search(0, y, lambda j: "1" in [image[i][j] for i in range(top, bottom)])  #直接range(len(image))也一样的.
        right = self.search(y + 1, len(image[0]), lambda j: "1" not in [image[i][j] for i in range(top, bottom)])    #边界+1
        return (right - left) * (bottom - top)

    def search(self, i, j, check):
        while i < j:
            mid = (i + j) / 2
            if check(mid):  j = mid #满足的话, mid可能是.
            else:   i = mid + 1  #不满足. mid不可能是
        return i