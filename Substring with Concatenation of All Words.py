class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        lenS = len(S); lenL = len(L); lenWord = len(L[0])
        result = []  #因为都是相同的长度，所以直接按照该长度来分割成array就好。
        for start in range(lenS - lenWord * lenL + 1):
            listS = [S[i : i+lenWord] for i in range(start, start + lenL * lenWord  , lenWord) ] # split [start, start+n*Word] to n words
            found = True
            for item in L:
                if item in listS:
                    listS.remove(item)
                else:
                    found = False
                    break
            if found:result.append(start)
        return result