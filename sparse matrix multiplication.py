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

class Solution:
    def multiply(self, A, B):  # 1X3   , 3X1 , 有衔接.
        cols = [[(j, x) for j, x in enumerate(col) if x] for col in zip(*B)]
        return [[sum(row[j]*x for j, x in col if row[j]) for col in cols]  for row in A]


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