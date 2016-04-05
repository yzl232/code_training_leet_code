'''
 You are given an array x of n positive numbers. You start at point (0,0) and moves x[0] metres to the north, then x[1] metres to the west, x[2] metres to the south, x[3] metres to the east and so on. In other words, after each move your direction changes counter-clockwise.

Write a one-pass algorithm with O(1) extra space to determine, if your path crosses itself, or not.

Example 1:

Given x = [2, 1, 1, 2],
┌───┐
│   │
└───┼──>
    │

Return true (self crossing)

Example 2:

Given x = [1, 2, 3, 4],
┌──────┐
│      │
│
│
└────────────>

Return false (not self crossing)

Example 3:

Given x = [1, 1, 1, 1],
┌───┐
│   │
└───┼>

Return true (self crossing)

'''


class Solution(object):
    def isSelfCrossing(self, x):
        return any(d >= b > 0 and (a >= c or a >= c-e >= 0 and f >= d-b)
                   for a, b, c, d, e, f in ((x[i:i+6] + [0] * 5)[:6]
                                            for i in xrange(len(x))))
                                            
'''
Explanation

            b                              b
   +----------------+             +----------------+
   |                |             |                |
   |                |             |                | a
 c |                |           c |                |
   |                | a           |                |    f
   +----------->    |             |                | <----+
            d       |             |                |      | e
                    |             |                       |
                                  +-----------------------+
                                               d

Draw a line of length a. Then draw further lines of lengths b, c, etc. How does the a-line get crossed? From the left by the d-line or from the right by the f-line, see the above picture. I just encoded the criteria for actually crossing it.

Two details:

    In both cases, d needs to be at least b. In the first case to cross the a-line directly, and in the second case to get behind it so that the f-line can cross it. So I factored out d >= b.
    The "special case" of the e-line stabbing the a-line from below is covered because in that case, the f-line "crosses" it (note that even if there is no actual f-line, my code uses f = 0 and thus still finds that "crossing").

'''