class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        br_dict = {')':'(','}':'{',']':'['}
        br = []
        for i in s:
            if i in br_dict:
                if len(br)==0 or br[-1] != br_dict[i]:
                    return False
                br.pop()    
            else: br.append(i)   
        return len(br)==0


        