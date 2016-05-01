'''
Group Shifted Strings 

Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"

Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Return:

[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]

Note: For the return value, each inner list's elements must follow the lexicographic order.

给的例子太不具说明性了。应该举这个例子：

["eqdf", "qcpr"]。

((‘q’ - 'e') + 26) % 26 = 12, ((‘d’ - 'q') + 26) % 26 = 13, ((‘f’ - 'd') + 26) % 26 = 2

((‘c’ - 'q') + 26) % 26 = 12, ((‘p’ - 'c') + 26) % 26 = 13, ((‘r’ - 'p') + 26) % 26 = 2

所以"eqdf"和"qcpr"是一组shifted strings。
'''
class Solution:
    def groupStrings(self, arr):
        d = collections.defaultdict(list)
        for s in arr: #不能-ord("A"), 本题特点-ord(s[0])合适
            d[tuple((ord(ch) - ord(s[0]) + 26) % 26 for ch in s)].append(s)
        return [sorted(x) for x in d.values()]
'''
class Solution:
    def groupStrings(self, arr):
        d = {}
        for s in arr:
            t = tuple((ord(ch) - ord(s[0]) + 26) % 26 for ch in s)
            if t not in d: d[t] = []
            d[t].append(s)
        return [sorted(x) for x in d.values()]

s = Solution()
print s.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])
        
>>> defaultdict(list)
defaultdict(<type 'list'>, {})
>>> defaultdict(set)
defaultdict(<type 'set'>, {})
>>> defaultdict(dict)
defaultdict(<type 'dict'>, {})
>>> defaultdict(int)
defaultdict(<type 'int'>, {})
>>> defaultdict(lambda: 1)
defaultdict(<function <lambda> at 0x10eea7b90>, {})
'''