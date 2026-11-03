class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {']':'[','}':'{',')':'('}
        stack = deque()
        for i in s:
            if i in brackets and len(stack)>0 and brackets[i]==stack[-1]:
                stack.pop()
            else: stack.append(i)
        return not len(stack)