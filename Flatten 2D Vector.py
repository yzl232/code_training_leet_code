'''


    Implement an iterator to flatten a 2d vector.

    For example, Given 2d vector =

    [
      [1,2],
      [3],
      [4,5,6]
    ] 

    By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5,6].

'''
#做过。 见flatten iterator文件。 那个文件很多好代码
#只是2D。  容易些。

class Vector2D:
    # Initialize your data structure here.
    # @param {integer[][]} vec2d
    def __init__(self, vec2d):
        self.c = self.r = 0
        self.vec = vec2d

    # @return {integer}
    def next(self):
        ret = self.vec[self.r][self.c]
        self.c += 1
        return ret

    # @return {boolean}
    def hasNext(self):
        while self.r < len(self.vec):
            if self.c < len(self.vec[self.r]):   return True
            self.c = 0
            self.r += 1
        return False

