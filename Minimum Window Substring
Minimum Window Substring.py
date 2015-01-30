'''
 Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"

Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the emtpy string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
'''

#通用性最好的。
class Solution:
    # @return a string
    def minWindow(self, s, t):
        m = len(s); n = len(t); ret = ('', m+1)   #关键是用了2个hashtable。 另外缩减窗口。
        fdN = 0; tcnt ={}; fndD = {}; l = 0   #到达了长度，就一直尝试缩减窗口
        for x in t:
            if x not in tcnt: tcnt[x]=0
            tcnt[x]+=1
        for r in range(m):
            x = s[r]
            if x not in tcnt: continue
            if x not in fndD or tcnt[x] > fndD[x]: fdN+=1    #fndC之后不会再动了
            if x not in fndD:  fndD[x]=0
            fndD[x]+=1    #这两行照抄上面tcnt部分的
            if fdN == n:  #has
                x = s[l]
                while x not in tcnt or fndD[x] > tcnt[x]:   #这也是和上面那句类似的。 方向相反。
                    if s[l] in tcnt: fndD[s[l]] -=1
                    l +=1; x=s[l]
                if r - l +1 < ret[-1]:   ret = (s[l: r+1], r-l+1)
        return ret[0]


'''
class Solution:
    # @return a string
    def minWindow(self, s, t):
        m = len(s); n = len(t); ret = ''
        if m<n or n==0: return ''
        need=[0]*128; cnt=0; l=0; minL=len(s)+1
        for ch in t:  need[ord(ch)]+=1
        for r in range(m):
            if need[ord(s[r])]>0: cnt+=1
            need[ord(s[r])]-=1
            while cnt==n:
                if r - l +1 < minL:
                    ret = s[l: r+1]
                    minL = r - l +1
                need[ord(s[l])]+=1       # cnt+=1, -=1, +=1, cnt-=1 有对称。。
                if need[ord(s[l])]>0: cnt-=1
                l+=1
        return ret



class Solution:
    # @return a string
    def minWindow(self, s, t):
        m = len(s); n = len(t); ret = ''
        if m<n: return ''  #到达了长度，就一直尝试缩减窗口
        l = 0; minL = m+1  #关键是用了2个hashtable。 另外缩减窗口。
        fdN = 0; need ={}
        for ch in t:
            if ch not in need: need[ch]=0
            need[ch]+=1
        for r in range(m):
            if s[r] not in need: continue
            if need[s[r]] > 0: fdN+=1    #fndC之后不会再动了。window一直是valid
            need[s[r]]-=1
            if fdN>=n:     #fdN作用不大。   因为window一直是valid的。
                while s[l] not in need or need[s[l]]<0:
                    if s[l] in need: need[s[l]]+=1
                    l+=1
                if r - l +1 < minL:
                    ret = s[l: r+1]
                    minL = r - l +1
        return ret



'''


