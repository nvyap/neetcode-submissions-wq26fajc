class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {']':'[','}':'{',')':'('}
        res = []
        for i in s:
            if i in brackets and len(res)>0 and brackets[i] == res[-1]:
                res.pop()
            else: res.append(i)
        return len(res)==0
            

        