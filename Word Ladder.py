class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        dict.add(end)
        wordLen = len(start)
        candidates = set()
        candidates.add((start, 1))
        while True:
            if len(candidates)==0:  break
            current = set()
            for cur in candidates:
                curWord = cur[0];curLen = cur[1]
                if curWord == end:return curLen
                for i in range(wordLen):
                    part1 = curWord[:i]; part2 = curWord[i+1:] # replace ith char
                    #print part1, part2
                    for j in 'abcdefghijklmnopqrstuvwxyz': # BFS
                        if curWord[i] !=j:
                            nextWord = part1 + j + part2
                            #print nextWord
                            if nextWord == end: return curLen+1
                            if nextWord in dict:
                                current.add((nextWord, curLen + 1))
                                dict.remove(nextWord)
            candidates = current
        return 0