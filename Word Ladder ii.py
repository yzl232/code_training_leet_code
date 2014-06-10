class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        self.start = start
        self.result = []
        self.preMap = {}
        l = len(start)
        for i in dict:
            self.preMap[i] = []
        candidates =set([])
        candidates.add(start)
        while True:
            if len(candidates) == 0:
                return []
            if end in candidates:
                break
            for i in candidates:
                dict.remove(i)
            current = set([])
            for word in candidates:
                for i in range(l):
                    part1 = word[:i]
                    part2 = word[i+1:]
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        if word[i] != j:
                            nextword = part1 + j + part2
                            if nextword in dict:
                                self.preMap[nextword].append(word)
                                current.add(nextword)
            candidates = current
        self.buildPath([], end)
        return self.result

    def buildPath(self, path, word):
        if word == self.start:   
            temp = path + [word]
            self.result.append(temp[::-1])
            return
        for it in self.preMap[word]:
            self.buildPath(path+[word], it)