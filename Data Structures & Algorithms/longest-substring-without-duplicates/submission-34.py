class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        queue = deque()
        seen = set()
        max_len = 0
        for i in s:
            while i in seen:
                seen.discard(queue.popleft())
            seen.add(i)
            queue.append(i)
            max_len = max(max_len, len(queue))
        return max_len
        

        