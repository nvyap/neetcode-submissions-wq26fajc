class Solution:
    def isValid(self, s: str) -> bool:
        iter_lst = []
        
        hs = {')':'(',']':'[','}':'{'}
        for i in s:
            if i in hs and len(iter_lst)>0 and hs[i] == iter_lst[-1]:
                iter_lst.pop()
            else:
                iter_lst.append(i)
        if len(iter_lst)==0:
            return True
        return False

        