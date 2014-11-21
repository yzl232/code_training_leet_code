'''
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
'''

class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        paths = path.split('/')
        results = ''
        for i in paths:
            if i!= '..' and i!='' and i!='.':
                results += '/'+i
            elif i=='..':
                if results != '':
                    results = '/'.join(results.split('/')[:-1])
        return results if results !='' else '/'