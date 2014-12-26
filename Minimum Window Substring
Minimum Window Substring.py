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
        ls = len(s); lt = len(t); ret = ''
        if ls<lt: return ''  #到达了长度，就一直尝试缩减窗口
        st = 0; minL = ls+1  #关键是用了2个hashtable。 另外缩减窗口。
        fdN = 0; tcnt ={}; fnd = {}
        for ch in t:
            if ch not in tcnt: tcnt[ch]=0
            tcnt[ch]+=1
        for end in range(ls):
            ch = s[end]
            if ch not in tcnt: continue
            if ch not in fnd or tcnt[ch] > fnd[ch]: fdN+=1    #fndC之后不会再动了
            if ch not in fnd:  fnd[ch]=0
            fnd[ch]+=1    #这两行照抄上面tcnt部分的
            if fdN == lt:  #has
                while s[st] not in tcnt or fnd[s[st]] > tcnt[s[st]]:
                    if s[st] in t: fnd[s[st]] -=1
                    st +=1
                if end - st +1 < minL:
                    ret = s[st: end+1]
                    minL = end - st +1
        return ret