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
                if cur == pre:
                    num+=1                    
                else:
                    newS+= str(num) + pre# finish counting the prev ch, update
                    num = 1
                    pre = cur
            newS += str(num) + pre # string ends, update 
            s = newS
        return s