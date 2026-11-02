class Solution:
    def isValid(self, s: str) -> bool:
        seen = deque()
        brackets = {']':'[',')':'(','}':'{'}
        for i in s:
            if i in brackets:
                if not seen or seen[-1]!=brackets[i]:
                    return False
                seen.pop()
                
            else:
                seen.append(i)
                #print(f'appended={seen}')
        return not len(seen)


        