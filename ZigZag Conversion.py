'''
 The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);

convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''
class Solution:
    # @return a string
    def convert(self, s, r):
        if r <=1: return s
        zigN = r *2 - 2
        ret = ''; n = len(s)
        for i in range(r):
            base = i
            while base < n:
                ret+=s[base]
                base += zigN
                if i not in (0, r-1) and base-2*i< n:ret += s[base-2*i]
        return ret