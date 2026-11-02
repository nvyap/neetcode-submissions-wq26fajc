class Solution:
    def isValid(self, s: str) -> bool:
        seen = deque()
        brackets = {']':'[',')':'(','}':'{'}
        for i in s:
            if i in brackets and len(seen)>0 and brackets[i] == seen[-1]:
                #print(seen)
                seen.pop()
                
            else:
                seen.append(i)
                #print(f'appended={seen}')
        return not len(seen)


        