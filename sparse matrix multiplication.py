'''
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

    A = [
      [ 1, 0, 0],
      [-1, 0, 3]
    ]

    B = [
      [ 7, 0, 0 ],
      [ 0, 0, 0 ],
      [ 0, 0, 1 ]
    ]


     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
              | 0 0 1 |

'''

# encoding=utf-8
class Solution:  #只存i不存j
    def multiply(self, a, b):  # 1X3   , 3X1 , 有衔接.
        cols = [[(r, x) for r, x in enumerate(col) if x] if any(col) else [] for col in zip(*b)]  #col帅选掉了很多计算了.
        return [[sum(row[j]*x for j, x in col) for col in cols] if any(row) else [0]*len(row) for row in a]

#需要复习矩阵乘法。 对应的行与对应的列相乘

'''
稀疏vector的点乘
#facebook这道题目。 可以这样。只储存非0的value.    (val, index). sort by index
class Solution:  #  (val, index).
    def multip(self, v1, v2):
        ret =[];  i=j=0
        while i<len(v1) and j<len(v2):
            x1, x2 = v1[i][-1], v2[j][-1]
            if x1==x2:    ret.append(   (v1[i][0]*v2[j][0], x1  )    )
            elif x1<x2:  i+=1
            else: j+=1
        return ret
'''
        
'''
稀疏vector的点乘
#facebook这道题目。 可以这样。只储存非0的value.    (val, index). sort by index
class Solution:  #  (val, index).
    def multip(self, v1, v2):
        ret =[];  i=j=0
        while i<len(v1) and j<len(v2):
            x1, x2 = v1[i][-1], v2[j][-1]
            if x1==x2:    ret.append(   (v1[i][0]*v2[j][0], x1  )    )
            elif x1<x2:  i+=1
            else: j+=1
        return ret
'''
s = Solution()
A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]
print s.multiply(A, B)