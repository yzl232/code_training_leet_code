class Solution:
    def shortestDistance(self, words, word1, word2):
        last, ret = -1, len(words)
        for i in range(len(words)):
            if words[i] in [word1, word2]:
                if last != -1 and (words[last] != words[i]): # if current matched word is different from last matched word
                    ret = min(ret, i-last)
                last = i
        return ret




#为了与三保持一致, 改用一个pointer
'''
class Solution(object):
    def shortestDistance(self, words, word1, word2):# one pass
        p1 = p2 = -1; ret = len(words)+1
        for i in range(len(words)):
            if words[i] == word1:  p1 = i
            if words[i] == word2: p2 = i
            if p1!= -1 and p2!=-1:  ret = min(ret, abs(p1-p2))
        return ret


class Solution(object):
    def shortestDistance(self, words, word1, word2):
        return min(abs(i - j) for i in xrange(len(words)) if words[i] == word1 for j in xrange(len(words)) if words[j] == word2)
'''


'''
#geeks做过。   
Find the minimum distance between two numbers
'''