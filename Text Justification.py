class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        firstWord =0
        numWords = 0
        caractersInLine = 0
        result = []
        for i in range(0,len(words)):
            if caractersInLine + numWords + len(words[i])>L:
                line = []
                if numWords == 1:
                    line.append(words[firstWord])
                    for n in range(len(words[firstWord]), L):
                        line.append(' ')
                elif numWords - 1>0:
                    spaces = (L-caractersInLine) // (numWords-1)
                    extraspaces = (L-caractersInLine) % (numWords-1)
                    for j in range(firstWord, i):
                        line.append(words[j])
                        if j == i-1:  break    
                        for n in range(0, spaces):
                            line.append(' ')
                        if j-firstWord < extraspaces:
                            line.append(' ')
                result.append(''.join(line))
                firstWord =i
                numWords = 0
                caractersInLine = 0
            numWords += 1
            caractersInLine += len(words[i])
        if firstWord < len(words):
            line =[]
            for j in range(firstWord, len(words)):
                line.append(words[j])
                if j == len(words)-1:  break
                line.append(' ')
            for n in range(len(''.join(line)),L):
                line.append(' ')
            result.append(''.join(line))
        return result