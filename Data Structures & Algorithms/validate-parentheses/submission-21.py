class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {']':'[','}':'{',')':'('}
        res = []
        for i in s:
            if i in brackets:
                if res and brackets[i] == res[-1]:
                    res.pop()
                else: return False
            else: res.append(i)
        return len(res)==0
            

        