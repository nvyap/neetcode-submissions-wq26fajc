class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        tar = []
        op = ['(','{','[']
        cl = [')',']','}']
        bracket_map = {")": "(", "]": "[", "}": "{"}
        for i in s:
            if i in op:
                tar.append(i)
            l = len(tar)-1
            
            if i in cl:
                if l <0 : return False
                if bracket_map[i]!=tar[l]:
                    return False
                tar.pop()
        return len(tar)==0
        