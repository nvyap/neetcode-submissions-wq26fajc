class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')':'(',']':'[','}':'{'}
        track_brackets = []
        for i in s:
            if i not in brackets:
                track_brackets.append(i)
            elif i in brackets:
                if len(track_brackets)==0 or track_brackets[-1]!= brackets[i]:
                    return False
                else:
                    track_brackets.pop()
        return not track_brackets
    

        