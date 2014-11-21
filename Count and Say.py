'''
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
'''
class Solution:
    # @return a string
    def countAndSay(self, n):
        s = '1'
        for i in range(n-1):
            newS = ''
            pre = s[0]
            num = 1
            for j in range(1, len(s)):
                cur = s[j]
                if cur == pre: #核心就在这里。 一样的数字，统计。  不一样，立刻更新输出
                    num+=1
                else:
                    newS+= str(num) + pre# finish counting the prev ch, update
                    num = 1
                    pre = cur
            newS += str(num) + pre # string ends, update
            s = newS
        return s