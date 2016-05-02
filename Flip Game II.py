'''
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip twoconsecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to determine if the starting player can guarantee a win.

For example, given s = "++++", return true. The starting player can guarantee a win by flipping the middle "++" to become "+--+".

Follow up:
Derive your algorithm's runtime complexity.
'''


class Solution(object):
    memo = {}
    def canWin(self, s):
        if s not in self.memo:
            self.memo[s] = any(s[i:i+2] == '++' and not self.canWin(s[:i] + '-' + s[i+2:])
                          for i in range(len(s)-1)) 
        return self.memo[s]
# 不能放在if里面， 不然any()里面可能为空


'''

class Solution(object):
    def canWin(self, s):
        return any(s[i:i+2] == '++' and not self.canWin(s[:i] + '--' + s[i+2:])
                   for i in range(len(s)))
                   
                   
'''