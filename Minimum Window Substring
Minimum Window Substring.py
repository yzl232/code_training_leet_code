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


class Solution:
    # @return a string
    def minWindow(self, s, t):
        m = len(s); n = len(t); ret = ''
        if m<n: return ''  #到达了长度，就一直尝试缩减窗口
        l = 0; minL = m+1  #关键是用了2个hashtable。 另外缩减窗口。
        fdN = 0; tcnt ={}; fnd = {}
        for ch in t:
            if ch not in tcnt: tcnt[ch]=0
            tcnt[ch]+=1
        for r in range(m):
            ch = s[r]
            if ch not in tcnt: continue
            if ch not in fnd or tcnt[ch] > fnd[ch]: fdN+=1    #fndC之后不会再动了
            if ch not in fnd:  fnd[ch]=0
            fnd[ch]+=1    #这两行照抄上面tcnt部分的
            if fdN == n:  #has
                while s[l] not in tcnt or fnd[s[l]] > tcnt[s[l]]:
                    if s[l] in t: fnd[s[l]] -=1
                    l +=1
                if r - l +1 < minL:
                    ret = s[l: r+1]
                    minL = r - l +1
        return ret


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


