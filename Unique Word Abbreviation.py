'''
Unique Word Abbreviation
Total Accepted: 351 Total Submissions: 2106 Difficulty: Easy

An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
d) l|ocalizatio|n          --> l10n

Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

Example:

Given dictionary = [ "deer", "door", "cake", "card" ]

isUnique("dear") -> false
isUnique("cart") -> true
isUnique("cane") -> false
isUnique("make") -> true


'''


class ValidWordAbbr(object):
    def __init__(self, arr):  #相同的word出现多次, 仍然算是unique. 所以用set.
        self.d = {}
        for w in arr:
            k = self.abbr(w)  #len(w)和len(w)-2之间没有区别。
            if k not in self.d: self.d[k] = set()
            self.d[k].add(w)

    def isUnique(self, w):
        k = self.abbr(w)   #本来想写len(self.dt[k])==1 发现错了,  必需考虑word相等. 比如dig, dog都是d1g
        return k not in self.d or set([w]) == self.d[k]

    def abbr(self, w):
        return w if len(w)<=2 else w[0] + str(len(w)) + w[-1]