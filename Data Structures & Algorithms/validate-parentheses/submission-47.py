class Solution:
    def isValid(self, s: str) -> bool:
        queue = deque()
        brackets_hash = {')':'(',']':'[','}':'{'}
        for i in s:
            if i in brackets_hash:
                if queue and queue[-1] == brackets_hash[i]:
                    queue.pop()
                else:
                    return False
            else: 

                queue.append(i)
        if len(queue)!=0:
            return False
        return True

        