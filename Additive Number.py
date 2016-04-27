'''
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

For example:
"112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.

1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

"199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.

1 + 99 = 100, 99 + 100 = 199

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Follow up:
How would you handle overflow for very large input integers? 
'''

class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if num is None or len(num) < 3:  return False
        n = len(num)
        for i in range(1, n):
            if i > 1 and num[0] == '0':   break
            for j in range(i+1, n):
                first, second, third = 0, i, j
                if num[second] == '0' and third > second + 1:   break
                while third < n:
                    result = str(int(num[first:second]) + int(num[second:third]))
                    if num[third:].startswith(result):
                        first, second, third = second, third, third + len(result)
                    else:  break
                if third == n: return True
        return False