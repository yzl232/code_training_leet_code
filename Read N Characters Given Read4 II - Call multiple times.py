'''
 The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
The read function may be called multiple times.


'''

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution:
    # @param buf, Destination buffer (a list of characters)
    # @param n,   Maximum number of characters to read (an integer)
    # @return     The number of characters read (an integer)
    def __init__(self):  # tmpBuf存的总量  If bufsize > 0, that means there is partial data left in buffer
        self.i=self.n = 0   #上次读到哪里了
        self.buf = [None] * 4

    def read(self, buf, n):
        i = 0
        while i<n:      #tmp的作用就是判断是不是4。
            if self.i==self.n:
                self.n, self.i= read4(self.buf), 0           #变化就是tmpN变成了self.tmpN,  i变成了self.i, 三个都成了self.
                if self.n==0: break
            while i<n and self.i<self.n:
                buf[i]=self.buf[self.i]
                i+=1;  self.i+=1
        return i


'''
# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution:
    # @param buf, Destination buffer (a list of characters)
    # @param n,   Maximum number of characters to read (an integer)
    # @return     The number of characters read (an integer)
    def __init__(self):
        self.offset = 0
        self.bufsize = 0 #If bufsize > 0, that means there is partial data left in buffer .我们直接复制这里就好。不用call read4k
        self.tmpBuffer = [None for i in range(4)]

    def read(self, buf, n):
        count = 0; tmpN = 4; flag = True
        while n > count and flag:#tmp的作用就是判断是不是4。
            if self.bufsize!=0:  tmpN = self.bufsize
            else:
                tmpN = read4(self.tmpBuffer)
                if tmpN<4: flag = False
            byteN = min(tmpN, n-count)
            buf[count:count+byteN]= self.tmpBuffer[self.offset:self.offset+byteN]  #结束的2个指标 。  1 tmp!=4.   或者n<=count 读完了。 因为我们目标是读n个。
            self.offset = (self.offset+byteN) % 4
            self.bufsize = tmpN - byteN  #就是判断有没有残余。   也就是n-count < tmpN吗？
            count+=byteN
        return count
'''