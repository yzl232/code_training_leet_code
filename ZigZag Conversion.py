class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows <=1: return s
        zigSize = nRows *2 - 2
        results = ''; n = len(s)
        for i in range(nRows):
            base = i
            while base < n:
                results+=s[base]
                base += zigSize
                if i>0 and i<nRows-1:
                    temp = base-2*i
                    if temp < n: results += s[temp]
        return results