# encoding=utf-8

'''


    A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

    For example, given three people living at (0,0), (0,4), and (2,2):

    1 - 0 - 0 - 0 - 1
    |   |   |   |   |
    0 - 0 - 0 - 0 - 0
    |   |   |   |   |
    0 - 0 - 1 - 0 - 0

    The point (0,2) is an ideal meeting point, as the total travel
    distance of 2+2+2=6 is minimal. So return 6.

'''
#G家超高频。  有障碍物，没障碍物两种。 搜障碍或者搜健身房  py文件

'''
#这里的距离采用曼哈顿距离——|x0-x1| + |y0-y1|
#因为采用曼哈顿距离，所以可以分开考虑x坐标和y坐标。将k个点的x坐标排序，可以知道要求的x坐标一定在这k个点的x坐标上，

#实际上是取x坐标的中位数。   需要排好序
# 。对y坐标做同样的操作，从而得到答案。时间复杂度O(klogk)，排序的复杂度。
# 基于qiuck select的方法找median可以吧
#非常快。  用O(k)就可以了。 比O(k*n^2). 当然，也可以提一下。加分。
'''

#如果有障碍用BFS。 

#如果有障碍用BFS。 
class Solution:
    def minTotalDistance(self, grid):
        m, n = len(grid), len(grid[0])
        x, y = [i for i in range(m) for j in range(n) if grid[i][j]], [j for j in range(n) for i in range(m) if grid[i][j]]
        return sum(abs(i-x[len(x)/2])+abs(j-y[len(y)/2]) for i in range(m) for j in range(n) if grid[i][j])
#  这个顺序, y 是先range(n)再range(m).  必须分开求x, y.    这样避免了排序

#如果只是找点, 用quick select      .  总体只要O(m)+O(n)
s = Solution()
print s.minTotalDistance([[0, 1], [1, 1]])

