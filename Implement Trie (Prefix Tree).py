#最简单的最好的
class Trie:  #和以前的做法的区别是以前用_end存的, 现在用Trie Node存的.  没啥区别.

    def __init__(self):
        self.root = {}

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur:   cur[ch] = {}
            cur = cur[ch]
        cur["#"] = "#"

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):   #正常的话, 要考个DFS. 返回所有的.
        x = self.retrieve(word)
        return x!=None and "#" in x

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        return self.retrieve(prefix)!=None

    def retrieve(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur: return
            cur = cur[ch]
        return cur

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")

'''
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
    def search(self, word):   #正常的话, 要考个DFS. 返回所有的.
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


# encoding=utf-8

insert(key, value)
has

简单的说，我这里的implementation就是以每个letter为key的hashmap

也可以用node来实现trie


最简单的方法。
  for a large, scalable trie, nested dictionaries might become cumbersome -- or at least space inefficient
      
'''


'''
#典型应用是用于统计，排序和保存大量的字符串（但不仅限于字符串），所以经常被搜索引擎系统用于文本词频统计。它的优点是：利用字符串的公共前缀来减少查询时间，最大限度地减少无谓的字符串比较，查询效率比哈希表高

#trie用到的没有那么多。 主要就是prefix相关的题目


_end = '_end_'
class Trie:   #30多行。 主要是hashtable和DFS。   不难
    def makeTrie(self, words):
        root = {}
        for word in words:
            self.insert(word, root)
        return root

    def insert(self, word, root):  #这两个函数用的多
        cur = root
        for ch in word:
            if ch not in cur:   cur[ch] = {}
            cur = cur[ch]
        cur[_end] = _end  #end的value可以用来存储东西。。。

    def inTrie(self, trie, word):
        branch = self.retrieveBranch(trie, word)
        if branch and _end in branch: return True
        return False

    def retrieveBranch(self, trie, word):#这两个函数用的多
        cur = trie
        for ch in word:
            if ch not in cur: return    #和insert基本上一样
            cur = cur[ch]
        return cur

    def startWith(self, trie, prefix):  #太适合用recursion了。 想了半天，用recursion取最合适。 也不用修改原来的结构。
        self.ret = [];
        branch = self.retrieveBranch(trie, prefix)  #先找到目前匹配的。
        self.dfs(branch, prefix)     #dfs寻找所有的。prefix作为cur来用
        return self.ret

    def dfs(self, trie, cur):
        if not trie:  return
        for key in trie:
            if key == _end:  self.ret.append(cur)
            else:   self.dfs(trie[key], cur+key)




t = Trie()
a = t.makeTrie(['foo', 'bar', 'baz', 'barz'])
print a
print t.inTrie(a, 'ba')
print t.inTrie(a, 'barz')
b = t.makeTrie(["the", "a", "there", "answer", "any", "by", "bye", "their"])
print b
print t.startWith(b, "th")
print t.startWith(b, "a")

                       root
                    /   \    \
                    t   a_   b
                    |   |     |
                    h   n   y_
                    |   |  \  |
                    e_ s  y_ e_
                 /  |   |
                 i  r   w
                 |  |   |
                r_  e_ e
                        |
                        r_

'''
