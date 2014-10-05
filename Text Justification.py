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