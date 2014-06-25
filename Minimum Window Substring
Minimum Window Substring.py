class Solution:
    # @return a string
    def minWindow(self, s, t):
        ls = len(s); lt = len(t);results = ''
        if ls<lt: return ''
        start = 0; minWindowLen = ls+1
        hasFound = 0; tCount ={}; countFound = {}
        for ch in t:
            tCount[ch] = tCount[ch]+1 if ch in tCount else 1
        for end in range(ls):
            ch = s[end]
            if ch not in tCount: continue
            if ch not in countFound or tCount[ch] > countFound[ch]: hasFound+=1
            countFound[ch] = 1 if ch not in countFound else countFound[ch]+1
            if hasFound == lt:
                while s[start] not in t or countFound[s[start]] > tCount[s[start]]:
                    if s[start] in t: countFound[s[start]] -=1
                    start +=1
                windowLen = end - start +1
                if windowLen < minWindowLen:
                    results = s[start: end+1]
                    minWindowLen = windowLen
        return results