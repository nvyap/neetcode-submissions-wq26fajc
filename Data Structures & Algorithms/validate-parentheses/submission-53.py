class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {']':'[','}':'{',')':'('}
        queue = deque()
        for i in s:
            if i in brackets and len(queue)>0 and brackets[i]==queue[-1]:
                queue.pop()
            else: queue.append(i)
        return not len(queue)