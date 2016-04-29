''' Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)

search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

Note:
You may assume that all words are consist of lowercase letters a-z.

click to show hint.
You should be familiar with how a Trie works. If not, please work on this problem: Implement Trie (Prefix Tree) first. 
'''
class WordDictionary(object):
    def __init__(self):
        self.root = {}

    def addWord(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur:   cur[ch] = {}
            cur = cur[ch]
        cur["#"] = '#'

    def dfs(self, d, word):
        if self.ret: return
        if not word:
            if "#" in d: self.ret=True
            return
        if word[0] == '.':
            for d1 in d.values():
                if d1!="#": self.dfs(d1, word[1:])
        elif word[0] in d:  self.dfs(d[word[0]], word[1:])

    def search(self, word):
        self.ret = False
        self.dfs(self.root, word)
        return self.ret

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")