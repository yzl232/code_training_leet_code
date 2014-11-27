'''
 You are given a string, S, and a list of words, L, that are all of the same length. Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.

For example, given:
S: "barfoothefoobarman"
L: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
'''
class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        lenS = len(S); n = len(L); lenWord = len(L[0])
        result = []  #因为都是相同的长度，所以直接按照该长度来分割成array就好。
        for start in range(lenS - lenWord * n + 1):
            listS = [S[i : i+lenWord] for i in range(start, start + n * lenWord  , lenWord) ] # split [start, start+n*Word] to n words
            for item in L:
                if item in listS:
                    listS.remove(item)
                else:    break
            if listS == []:result.append(start)
        return result