'''
 Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:

    Only one letter can be changed at a time
    Each intermediate word must exist in the dictionary

For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]

As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:

    Return 0 if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.

'''

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
'''
双向bfs会很快

class Solution:

    def ladderLength(self, start, end, dict):
        dict.add(end)

        current, distance, visited = [start], 1, {start:0}
        bcurrent, bdistance, bvisited = [end], 1, {end:0}
        while current and bcurrent:
            pre, bpre,next, bnext = [], [], [], []
            for word in current:
                for i in xrange(len(word)):
                    left, right = word[:i], word[i + 1:]
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        candidate = left + j + right
                        if candidate in dict and candidate not in visited:
                            visited[candidate] = 0
                            next.append(candidate)
            for word in next:
                if word in bpre:
                    return distance + bdistance - 1
                if word in bcurrent:
                    return distance + bdistance
            pre, current, distance = current, next, distance + 1


            for word in bcurrent:
                for i in xrange(len(word)):
                    left, right = word[:i], word[i + 1:]
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        candidate = left + j + right
                        if candidate in dict and candidate not in bvisited:
                            bvisited[candidate] = 0
                            bnext.append(candidate)
            for word in bnext:
                if word in pre:
                    return distance + bdistance - 1
                if word in current:
                    return distance + bdistance
            bpre, bcurrent, bdistance = bcurrent, bnext, bdistance + 1
        return 0

'''