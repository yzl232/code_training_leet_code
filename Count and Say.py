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
            s1=''; j=0
            while j<len(s):
                cnt=1
                while (j+1)<len(s) and s[j]==s[j+1]: #先写容易错的j+1<len(s)
                    j+=1;  cnt+=1   #先写容易忘的j+=1
                s1+=str(cnt)+s[j]
                j+=1 #先写容易忘的j+=1
            s=s1
        return s


'''
class Solution:
    # @return a string
    def countAndSay(self, n):
        s = '1'
        for i in range(n-1):
            s1='';  pre = s[0];   cnt=1
            for j in range(1, len(s)):
                if s[j]==pre: cnt+=1
                else:
                    s1+=str(cnt)+pre
                    cnt=1;   pre = s[j]
            s1+=str(cnt)+pre
            s=s1
        return s
'''