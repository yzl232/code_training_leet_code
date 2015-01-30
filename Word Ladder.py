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
        cnt= 1; pre= [start];    dict.add(end)
        while pre:
            cur = []
            for word in pre:
                if word == end:     return cnt
                for i in range(len(word)):
                    for x in 'abcdefghijklmnopqrstuvwxyz':
                        t = word[:i] + x + word[i + 1:]
                        if t in dict:
                            cur.append(t);  dict.remove(t)
            cnt += 1;   pre = cur
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