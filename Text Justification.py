'''
 Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:

[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Note: Each word is guaranteed not to exceed L in length.
'''
class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, x):
        ret = []; i=0; m = len(words)
        while i<m:
            n=l=0; line = words[i] # N words, this line,.    length of line
            while i+n+1<=m and l+n+len(words[i+n])<=x:   #正好n+1个词。n个空
                l+=len(words[i+n]);  n+=1
            line+=''.join(" "*( 1 if i+n ==m else ((x-l)/(n-1)+ (j<(x-l)%(n-1)) ) ) + words[i+1+j] for j in range(n-1))
            ret.append(line+' '*(x-len(line))) #补全     #n-1个 。 先空格，后单词。   #最后一行
            i+=n    #先写这行。容易忘。
        return ret

'''
class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, k):
        firstWord = 0;  ret = []  #考虑情况比较多。 主要是计算单词间的间隔，左边多少个是要多一个空格。 最后一行左对齐就好，间隔就一个空格
        numWords = 0; chInLine = 0
        for i in range(len(words)):
            if chInLine+ len(words[i]) + numWords-1  >= k:  # exceed already, so exclude words[i]
                line = []
                if  numWords == 1:    line.append(words[firstWord]+' '*(k-len(words[firstWord])))  # fill spaceNum to make the length L #补满
                elif numWords > 1:  # divided by numWords-1    #因为要除以这么多
                    spaceNum, extraSpaces = (k - chInLine) / (numWords-1), (k-chInLine) % (numWords-1)
                    for j in range(firstWord, i):
                        line.append(words[j])
                        if j == i-1:   break   # last word. Spaces are not needed.
                        line.append(' '*spaceNum)
                        if j - firstWord < extraSpaces: line.append(' ')   # left part with extra spaceNum
                ret.append(''.join(line))
                firstWord = i
                numWords = 0;  chInLine = 0
            numWords +=1;   chInLine +=len(words[i])
        line = []  # last line
        for j in range(firstWord, len(words)):    #其实和上面的是一回事。
            line.append(words[j])
            if j == len(words) - 1: break
            line.append(' ')
        line.append(' '*(k-len(''.join(line))))     # fill spaceNum to make the length L
        ret.append(''.join(line))
        return  ret
'''