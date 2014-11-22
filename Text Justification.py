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
    def fullJustify(self, words, L):
        firstWord = 0#考虑情况比较多。 主要是计算单词间的间隔，左边多少个是要多一个空格。 最后一行左对齐就好，间隔就一个空格
        numWords = 0
        charactersInLine = 0
        solution = []
        for i in range(0, len(words)):
            if charactersInLine+ len(words[i]) + numWords-1  >= L:  # exceed already, so exclude words[i]
                line = []
                if numWords > 1:  # divided by numWords-1
                    spaces = (L - charactersInLine) // (numWords-1)
                    extraSpaces = (L-charactersInLine) % (numWords-1)
                    for j in range(firstWord, i):
                        line.append(words[j])
                        if j == i-1:  # last word. Spaces are not needed.
                            break
                        for n in range(spaces):
                            line.append(' ')
                        if j - firstWord < extraSpaces:  # left part with extra spaces
                            line.append(' ')
                elif numWords == 1:
                    line.append(words[firstWord])
                    for n in range(len(words[firstWord]), L):
                        line.append(' ')  # fill spaces to make the length L
                solution.append(''.join(line))
                firstWord = i
                numWords = 0
                charactersInLine = 0
            numWords +=1
            charactersInLine +=len(words[i])
        line = []  # last line
        for j in range(firstWord, len(words)):
            line.append(words[j])
            if j == len(words) - 1: break
            line.append(' ')
        for n in range(len(''.join(line)), L):
            line.append(' ')     # fill spaces to make the length L
        solution.append(''.join(line))
        return  solution