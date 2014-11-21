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
        ls = len(s); lt = len(t);results = ''
        if ls<lt: return ''  #到达了长度，就一直尝试缩减窗口
        start = 0; minWindowLen = ls+1  #关键是用了2个hashtable。 另外缩减窗口。
        hasFound = 0; tCount ={}; countFound = {}
        for ch in t:
            tCount[ch] = tCount[ch]+1 if ch in tCount else 1
        for end in range(ls):
            ch = s[end]
            if ch not in tCount: continue
            if ch not in countFound or tCount[ch] > countFound[ch]: hasFound+=1
            countFound[ch] = 1 if ch not in countFound else countFound[ch]+1
            if hasFound == lt:
                while s[start] not in tCount or countFound[s[start]] > tCount[s[start]]:
                    if s[start] in t: countFound[s[start]] -=1
                    start +=1
                windowLen = end - start +1
                if windowLen < minWindowLen:
                    results = s[start: end+1]
                    minWindowLen = windowLen
        return results