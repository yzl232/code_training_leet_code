# encoding=utf-8
'''
 The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
The read function will only be called once for each test case.
'''
# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution:
    # @param buf, Destination buffer (a list of characters)
    # @param n,   Maximum number of characters to read (an integer)
    # @return     The number of characters read (an integer)
    def read(self, buf, n):
        tmpBuffer = [None for i in range(4)]
        count = 0; tmpN = 4; flag = True
        while n > count and flag:#tmp的作用就是判断是不是4096。
            tmpN = read4(tmpBuffer)
            if tmpN<4:  flag=False
            byteN = min(tmpN, n-count)
            buf[count:count+byteN]= tmpBuffer[:byteN]  #结束2个指标 : 1 tmp!=4096.   或者n<=count 完成目标是读n个。或者read4k读完了。
            count+=byteN
        return count