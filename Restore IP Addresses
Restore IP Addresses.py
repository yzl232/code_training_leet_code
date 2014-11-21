'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
'''
class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        self.result = []
        self.getIP('', s, 0)
        return self.result

    def getIP(self, currIP, s, currIndex):
        if currIndex == 3:
            if len(s)>0:
                if int(s)<=255 and str(int(s)) == s:
                    self.result.append(currIP + s)
            return
        else:
            for i in range(1, 4):
                if i>len(s): break
                cur = s[:i]
                if int(cur) <= 255 and str(int(cur)) == cur:
                    self.getIP(currIP + cur + '.',  s[i:], currIndex+1)
