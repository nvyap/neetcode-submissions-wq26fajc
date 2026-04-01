class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        br_close = [')','}',']']
        br_open = ['(','{','[']
        br_dict = {')':'(','}':'{',']':'['}
        br = []
        for i in s:
            print(br)
            #if i in br_close and len(br)>0 and br[-1]!=br_dict[i]:
            #    return False
            if i in br_open:
                br.append(i)
            if i in br_close and (br or [None])[-1]!=br_dict[i]:
                return False
            elif i in br_close and br[-1]==br_dict[i]:
                br.pop()
            #elif i in br_open:
            
            
        return len(br)==0



        