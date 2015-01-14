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
    def findSubstring(self, s, l):
        m = len(s); n = len(l); wLen = len(l[0])
        ret = []; tCnt={}  #因为都是相同的长度，所以直接按照该长度来分割成array就好。
        for w in l:
            if w not in tCnt: tCnt[w]=0
            tCnt[w]+=1
        for i in range(wLen):     #所以总复杂度是O(2*n/l*l)=O(n)
            fdN=0;  fnd={}; st=i
            for end in range(wLen+i, len(s)+1, wLen):  #len(s)+1,  end可以到len(s)
                w = s[end-wLen :end]
                if w not in tCnt: continue
                if w not in fnd or tCnt[w]>fnd[w]: fdN+=1
                if w not in fnd: fnd[w]=0
                fnd[w] +=1
                if fdN==len(l):
                    w1 = s[st:st+wLen]
                    while w1 not in tCnt or fnd[w1] > tCnt[w1]:
                        if w1 in tCnt: fnd[w1]-=1
                        st+=wLen
                        w1 = s[st:st+wLen]
                    if len(l)==(end-st)/wLen: ret.append(st)
        return ret

#比暴力法快N倍

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






这道题看似比较复杂，其实思路和Longest Substring Without Repeating Characters差不多。因为那些单词是定长的，所以本质上和单一个字符一样。和Longest Substring Without Repeating Characters的区别只在于我们需要维护一个字典，然后保证目前的串包含字典里面的单词有且仅有一次。思路仍然是维护一个窗口，如果当前单词在字典中，则继续移动窗口右端，否则窗口左端可以跳到字符串下一个单词了。假设源字符串的长度为n，字典中单词的长度为l。因为不是一个字符，所以我们需要对源字符串所有长度为l的子串进行判断。做法是i从0到l-1个字符开始，得到开始index分别为i, i+l, i+2*l, ...的长度为l的单词。这样就可以保证判断到所有的满足条件的串。因为每次扫描的时间复杂度是O(2*n/l)(每个单词不会被访问多于两次，一次是窗口右端，一次是窗口左端)，总共扫描l次（i=0, ..., l-1)，所以总复杂度是O(2*n/l*l)=O(n)，是一个线性算法。空间复杂度是字典的大小，即O(m*l)，其中m是字典的单词数量
'''



'''
最小滑动窗口(Java AC的代码是448ms)

因为L中所有单词的长度是一样的，这样根据wordLen，可以将S分为wordLen组，实际意思是这样的。
以题目中barfoothefoobarman举例，L中单词长度为3，可以分为
bar|foo|the|foo|bar|man
ba|rfo|oth|efo|oba|rma|n
b|arf|oot|hef|oob|arm|an
这样，针对每个分组，可以利用最小滑动窗口的思想，快速的判断是否包含需要的字符串。
'''