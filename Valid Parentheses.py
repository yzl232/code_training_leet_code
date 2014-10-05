class Solution:
    # @return a boolean
    def isValid(self, s):
        lefts = {'(':0, '{':1, '[':2}
        rights = {')':0, '}':1, ']':2}
        stack = []
        for ch in s:
            if ch in lefts:
                stack.append(lefts[ch])
            elif ch in rights:
                if len(stack) ==0 : return False
                elif stack[-1] == rights[ch]: stack.pop()
                else: return False
            else:
                return False
        if len(stack) > 0 :return False
        return True