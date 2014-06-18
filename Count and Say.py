class Solution:
    # @return a string
    def countAndSay(self, n):
        s = '1'
        for i in range(n-1):
            prev = newS = ''
            num = 0
            for cur in s:
                if prev != '' and prev != cur:  # if prev == '', do not update.
                    newS += str(num) + prev  # finish counting the prev ch, update
                    num = 1
                else:      
                    num+=1
                prev = cur 
            newS += str(num) + prev  # string ends, update 
            s = newS
        return s