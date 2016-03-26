class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.childs = {}
        self.isWord = False

class Trie:  #和以前的做法的区别是以前用_end存的, 现在用Trie Node存的.  没啥区别.

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.childs:   cur.childs[ch] = TrieNode()
            cur = cur.childs[ch]
        cur.isWord = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        x = self.retrieve(word)
        return x!=None and x.isWord

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        return self.retrieve(prefix)!=None

    def retrieve(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.childs: return
            cur = cur.childs[ch]
        return cur

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")