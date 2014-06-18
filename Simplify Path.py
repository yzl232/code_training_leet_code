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