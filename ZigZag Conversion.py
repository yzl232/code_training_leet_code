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
                    if base-2*i< n:results += s[base-2*i]
        return results