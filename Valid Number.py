'''
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
...
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. 

'''

class Solution:
    # @param s, a string
    # @return a boolean和atoi比较像
    # example  ===     -123.E+5     ====
    def isNumber(self, s):
        s+='#'; i=0
        while s[i] ==' ':     i+=1
        if s[i] in ('+', '-'): i+=1
        n1 = 0
        while'0'<=s[i]<='9':
                n1+=1;  i+=1
        if s[i] == '.': i+=1
        n2 = 0
        while'0'<=s[i]<='9':
                n2+=1;  i+=1
        if n1==n2==0: return False  #e左边不能完全没有数字
        if s[i] in ('e', 'E'):
            i+=1
            if s[i] in ('+', '-'): i+=1
            n3 = 0
            while '0'<=s[i]<='9':
                n3+=1;  i+=1
            if n3 == 0: return False  #如果出现e。不能完全没有数字
        while s[i] == ' ': i+=1
        return s[i] == '#'


'''
class Solution:
    # @param s, a string
    # @return a boolean
    # @finite automation
    def isNumber(self, s):  # http://www.cnblogs.com/zuoyuan/p/3703075.html
        INVALID=0; SPACE=1; SIGN=2; DIGIT=3; DOT=4; EXPONENT=5;
        #0invalid,1space,2sign,3digit,4dot,5exponent,6num_inputs
        transitionTable=[[-1,  0,  3,  1,  2, -1],    #0 no input or just spaces
                         [-1,  8, -1,  1,  4,  5],    #1 input is digits
                         [-1, -1, -1,  4, -1, -1],    #2 no digits in front just Dot
                         [-1, -1, -1,  1,  2, -1],    #3 sign
                         [-1,  8, -1,  4, -1,  5],    #4 digits and dot in front
                         [-1, -1,  6,  7, -1, -1],    #5 input 'e' or 'E'
                         [-1, -1, -1,  7, -1, -1],    #6 after 'e' input sign
                         [-1,  8, -1,  7, -1, -1],    #7 after 'e' input digits
                         [-1,  8, -1, -1, -1, -1]]    #8 after valid input input space
        state=0; i=0
        while i<len(s):
            inputtype = INVALID
            if s[i]==' ': inputtype=SPACE
            elif s[i]=='-' or s[i]=='+': inputtype=SIGN
            elif '0'<=s[i]<='9': inputtype=DIGIT
            elif s[i]=='.': inputtype=DOT
            elif s[i]=='e' or s[i]=='E': inputtype=EXPONENT

            state=transitionTable[state][inputtype]
            if state==-1: return False
            else: i+=1
        return state == 1 or state == 4 or state == 7 or state == 8


class Solution1:
    # @param s, a string
    # @return a boolean
    # example  ===     -123.E+5     ====
    def isNumber(self, s):
        s+='#'
        while s[0] ==' ':
            s = s[1:]
        if s[0] == '+' or s[0] == '-': s = s[1:]
        n1 = 0
        while'0'<=s[0]<='9':
                n1+=1
                s = s[1:]
        if s[0] == '.': s = s[1:]
        n2 = 0
        while'0'<=s[0]<='9':
                n2+=1
                s = s[1:]
        if n1==0 and n2==0: return False
        if s[0] == 'e' or s[0] == 'E':
            s = s[1:]
            if s[0] == '+' or s[0] == '-': s = s[1:]
            n3 = 0
            while '0'<=s[0]<='9':
                n3+=1
                s = s[1:]
            if n3 == 0: return False
        while s[0] == ' ': s = s[1:]
        return s == '#'
'''