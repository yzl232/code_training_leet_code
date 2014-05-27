class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, words):

        words = set(words)
        set_s = set([])
        for i in s:
            if i not in set_s:
                set_s.add(i)

        set_words = set([])
        for word in words:
            for i in word:
                if i not in set_words:
                    set_words.add(i)

        for i in set_s:
            if i not in set_words:
                return []


        self.datastore = {}
        results = []
        temp = self.wordBreakGenerator(s, words)
        if temp == [] :
            return []
        for i in temp:
            results.append(i[:-1])
        return results




    def wordBreakGenerator(self, s, words):
        if s in self.datastore:
            return self.datastore[s]
        if s == '':
            self.datastore[s]=[]
            self.datastore[s].append('')
            return self.datastore[s]
        else:
            for i in range(1, len(s)+1):
                sub = s[:i]
                if sub not in words: continue
                for others in self.wordBreakGenerator(s[i:], words):
                    if s not in self.datastore:
                        self.datastore[s] = []
                    self.datastore[s].append(sub + ' ' + others)
            if s in self.datastore:
                return self.datastore[s]
            return []


        